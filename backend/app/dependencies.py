"""Dependency Injection for FastAPI"""

from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from sqlalchemy.orm import Session
import logging
from datetime import datetime, timedelta

from app.database.database import SessionLocal
from app.config import settings
from app.services.auth_service import verify_token, decode_token
from app.models.user import User

logger = logging.getLogger(__name__)
security = HTTPBearer()


def get_db() -> Session:
    """Get database session dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(
    credentials: HTTPAuthCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """Get current authenticated user"""
    token = credentials.credentials
    
    try:
        payload = decode_token(token)
        user_id: str = payload.get("sub")
        
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except Exception as exc:
        logger.error(f"Token verification failed: {str(exc)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = db.query(User).filter(User.id == int(user_id)).first()
    
    if user is None or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """Get current active user"""
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )
    return current_user


def check_permission(
    required_roles: list = None,
    required_permissions: list = None
):
    """Dependency to check user roles and permissions"""
    async def verify_permission(
        current_user: User = Depends(get_current_active_user),
        db: Session = Depends(get_db)
    ) -> User:
        # Check roles
        if required_roles:
            user_roles = [role.name for role in current_user.roles]
            if not any(role in required_roles for role in user_roles):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Insufficient permissions for this operation"
                )
        
        # Check permissions
        if required_permissions:
            user_permissions = []
            for role in current_user.roles:
                user_permissions.extend([perm.name for perm in role.permissions])
            
            if not all(perm in user_permissions for perm in required_permissions):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Missing required permissions"
                )
        
        return current_user
    
    return verify_permission


def get_request_user(
    request: Request,
    db: Session = Depends(get_db)
):
    """Extract user from request (for logging and tracking)"""
    auth_header = request.headers.get("Authorization")
    
    if auth_header:
        try:
            token = auth_header.split(" ")[1]
            payload = decode_token(token)
            user_id = payload.get("sub")
            
            if user_id:
                user = db.query(User).filter(User.id == int(user_id)).first()
                return user
        except Exception:
            pass
    
    return None
