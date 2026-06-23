"""Workflow Model"""

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.database import Base


class Workflow(Base):
    """Workflow Model"""
    __tablename__ = "workflows"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    n8n_id = Column(String(100), unique=True, nullable=False)
    department = Column(String(100), nullable=False)
    status = Column(String(50), default="active")  # active, inactive, maintenance
    version = Column(Integer, default=1)
    config = Column(JSON)  # Store workflow configuration
    error_handling = Column(String(50), default="email")  # email, webhook, sms
    is_monitoring = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    executions = relationship("WorkflowExecution", back_populates="workflow")


class WorkflowExecution(Base):
    """Workflow Execution Model"""
    __tablename__ = "workflow_executions"
    
    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(Integer, ForeignKey('workflows.id'), nullable=False)
    execution_id = Column(String(100), unique=True, nullable=False)
    status = Column(String(50), nullable=False)  # running, completed, failed
    input_data = Column(JSON)
    output_data = Column(JSON)
    error_message = Column(Text, nullable=True)
    execution_time = Column(Integer)  # milliseconds
    started_at = Column(DateTime, nullable=False)
    completed_at = Column(DateTime, nullable=True)
    
    # Relationships
    workflow = relationship("Workflow", back_populates="executions")
