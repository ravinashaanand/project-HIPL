"""Request/Response Schemas"""

from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime


class LoginRequest(BaseModel):
    """Login request schema"""
    email: EmailStr = Field(..., description="User email")
    password: str = Field(..., min_length=8, description="User password")


class TokenResponse(BaseModel):
    """Token response schema"""
    access_token: str
    token_type: str = "bearer"
    user: dict


class UserBase(BaseModel):
    """Base user schema"""
    email: EmailStr
    full_name: str
    is_active: bool = True


class UserResponse(UserBase):
    """User response schema"""
    id: int
    roles: List[str]
    department: Optional[str]
    last_login: Optional[datetime]
    created_at: datetime
    
    class Config:
        from_attributes = True


class RoleBase(BaseModel):
    """Base role schema"""
    name: str
    description: Optional[str] = None


class RoleResponse(RoleBase):
    """Role response schema"""
    id: int
    
    class Config:
        from_attributes = True


class DepartmentBase(BaseModel):
    """Base department schema"""
    name: str
    code: str
    description: Optional[str] = None


class DepartmentResponse(DepartmentBase):
    """Department response schema"""
    id: int
    
    class Config:
        from_attributes = True


class WorkflowBase(BaseModel):
    """Base workflow schema"""
    name: str
    description: Optional[str] = None
    n8n_id: str
    department: str


class WorkflowResponse(WorkflowBase):
    """Workflow response schema"""
    id: int
    status: str
    version: int
    is_monitoring: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class AuditLogResponse(BaseModel):
    """Audit log response schema"""
    id: int
    user_id: Optional[int]
    action: str
    module: str
    resource_type: str
    resource_id: str
    timestamp: datetime
    
    class Config:
        from_attributes = True
