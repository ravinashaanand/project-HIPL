"""Authentication Endpoints"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import logging

from app.database.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse, UserResponse
from app.models.user import User
from app.services.auth_service import (
    authenticate_user,
    create_access_token,
    verify_password,
    get_password_hash
)
from app.dependencies import get_current_active_user

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    """
    User Login Endpoint
    
    Returns:
        - access_token: JWT token for authenticated requests
        - token_type: Type of token (Bearer)
        - user: User information
    """
    user = authenticate_user(db, request.email, request.password)
    
    if not user:
        logger.warning(f"Failed login attempt for email: {request.email}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    if not user.is_active:
        logger.warning(f"Login attempt by inactive user: {request.email}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )
    
    # Update last login
    user.last_login = datetime.utcnow()
    db.commit()
    
    # Create access token
    access_token = create_access_token(
        data={"sub": str(user.id), "email": user.email}
    )
    
    logger.info(f"Successful login for user: {user.email}")
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "is_active": user.is_active,
            "roles": [role.name for role in user.roles]
        }
    }


@router.get("/me", response_model=UserResponse)
async def get_current_user(
    current_user: User = Depends(get_current_active_user)
):
    """
    Get Current User Information
    
    Returns:
        - User details including roles and permissions
    """
    return {
        "id": current_user.id,
        "email": current_user.email,
        "full_name": current_user.full_name,
        "is_active": current_user.is_active,
        "last_login": current_user.last_login,
        "roles": [role.name for role in current_user.roles],
        "department": current_user.department.name if current_user.department else None
    }


@router.post("/logout")
async def logout(
    current_user: User = Depends(get_current_active_user)
):
    """
    User Logout Endpoint
    
    Note: Token is invalidated client-side
    """
    logger.info(f"User logged out: {current_user.email}")
    return {"message": "Successfully logged out"}
