"""User Model"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.database import Base

# Association tables for many-to-many relationships
user_role = Table(
    'user_role',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('role_id', Integer, ForeignKey('roles.id'))
)

role_permission = Table(
    'role_permission',
    Base.metadata,
    Column('role_id', Integer, ForeignKey('roles.id')),
    Column('permission_id', Integer, ForeignKey('permissions.id'))
)


class User(Base):
    """User Model"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=True)
    last_login = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    roles = relationship(
        "Role",
        secondary=user_role,
        back_populates="users"
    )
    department = relationship("Department", back_populates="users")
    audit_logs = relationship("AuditLog", back_populates="user")


class Role(Base):
    """Role Model"""
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(String(500))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    users = relationship(
        "User",
        secondary=user_role,
        back_populates="roles"
    )
    permissions = relationship(
        "Permission",
        secondary=role_permission,
        back_populates="roles"
    )


class Permission(Base):
    """Permission Model"""
    __tablename__ = "permissions"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    description = Column(String(500))
    module = Column(String(100), nullable=False)  # accounting, procurement, etc.
    action = Column(String(100), nullable=False)  # create, read, update, delete
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    roles = relationship(
        "Role",
        secondary=role_permission,
        back_populates="permissions"
    )
