"""Audit Log Model"""

from sqlalchemy import Column, Integer, String, Text, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.database import Base


class AuditLog(Base):
    """Audit Log Model for tracking all user actions"""
    __tablename__ = "audit_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    action = Column(String(100), nullable=False)  # CREATE, READ, UPDATE, DELETE
    module = Column(String(100), nullable=False)  # accounting, procurement, etc.
    resource_type = Column(String(100), nullable=False)  # invoice, purchase_order, etc.
    resource_id = Column(String(100), nullable=False)
    changes = Column(JSON)  # Store before/after changes
    ip_address = Column(String(50))
    user_agent = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Relationships
    user = relationship("User", back_populates="audit_logs")
