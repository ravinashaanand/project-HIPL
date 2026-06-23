"""Database Connection & Session Management"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool
import logging

from app.config import settings

logger = logging.getLogger(__name__)

# Create engine
engine = create_engine(
    settings.DATABASE_URL,
    poolclass=QueuePool,
    pool_size=settings.DATABASE_POOL_SIZE,
    max_overflow=settings.DATABASE_MAX_OVERFLOW,
    pool_pre_ping=True,
    echo=settings.APP_DEBUG
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()


def init_db():
    """Initialize database - create all tables"""
    try:
        # Import all models to ensure they are registered
        from app.models.user import User, Role, Permission
        from app.models.department import Department
        from app.models.workflow import Workflow, WorkflowExecution
        from app.models.audit_log import AuditLog
        
        # Create all tables
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Database tables created successfully")
        
        # Seed initial data
        seed_database()
        
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {str(e)}")
        raise


def seed_database():
    """Seed database with initial data"""
    from app.models.user import User, Role, Permission
    from app.models.department import Department
    from app.services.auth_service import get_password_hash
    
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(Role).first() is not None:
            logger.info("Database already seeded, skipping...")
            return
        
        # Create roles
        roles_data = [
            {"name": "System Administrator", "description": "Full system access"},
            {"name": "Finance Manager", "description": "Finance and Accounting"},
            {"name": "Procurement Manager", "description": "Procurement and Vendor Management"},
            {"name": "Production Manager", "description": "Production and Operations"},
            {"name": "Inventory Manager", "description": "Inventory and Warehouse Management"},
            {"name": "Logistics Manager", "description": "Logistics and Supply Chain"},
            {"name": "HR Manager", "description": "Human Resources and Administration"},
            {"name": "Quality Manager", "description": "Quality Control and Assurance"},
            {"name": "Sales Manager", "description": "Sales and Customer Management"},
            {"name": "Compliance Officer", "description": "Compliance and Legal"},
        ]
        
        roles = {}
        for role_data in roles_data:
            role = Role(**role_data)
            db.add(role)
            roles[role_data["name"]] = role
        
        db.commit()
        logger.info("✅ Roles created successfully")
        
        # Create departments
        departments_data = [
            {"name": "Finance", "code": "FIN", "description": "Accounting & Finance"},
            {"name": "Procurement", "code": "PROC", "description": "Procurement & Vendor Management"},
            {"name": "Production", "code": "PROD", "description": "Production & Operations"},
            {"name": "Inventory", "code": "INV", "description": "Inventory & Warehouse"},
            {"name": "Logistics", "code": "LOG", "description": "Logistics & Supply Chain"},
            {"name": "HR", "code": "HR", "description": "Human Resources"},
            {"name": "Quality", "code": "QA", "description": "Quality Control"},
            {"name": "Sales", "code": "SAL", "description": "Sales & Customer Management"},
            {"name": "Compliance", "code": "COMP", "description": "Compliance & Legal"},
        ]
        
        departments = {}
        for dept_data in departments_data:
            dept = Department(**dept_data)
            db.add(dept)
            departments[dept_data["code"]] = dept
        
        db.commit()
        logger.info("✅ Departments created successfully")
        
        # Create users
        users_data = [
            {
                "email": "admin@hemrajgroup.com",
                "full_name": "System Administrator",
                "password": "Admin@HIPL2026",
                "role_name": "System Administrator",
                "is_superuser": True
            },
            {
                "email": "finance@hemrajgroup.com",
                "full_name": "Finance Manager",
                "password": "Finance@HIPL2026",
                "role_name": "Finance Manager",
                "department_code": "FIN"
            },
            {
                "email": "procurement@hemrajgroup.com",
                "full_name": "Procurement Manager",
                "password": "Procurement@HIPL2026",
                "role_name": "Procurement Manager",
                "department_code": "PROC"
            },
            {
                "email": "production@hemrajgroup.com",
                "full_name": "Production Manager",
                "password": "Production@HIPL2026",
                "role_name": "Production Manager",
                "department_code": "PROD"
            },
            {
                "email": "inventory@hemrajgroup.com",
                "full_name": "Inventory Manager",
                "password": "Inventory@HIPL2026",
                "role_name": "Inventory Manager",
                "department_code": "INV"
            },
            {
                "email": "logistics@hemrajgroup.com",
                "full_name": "Logistics Manager",
                "password": "Logistics@HIPL2026",
                "role_name": "Logistics Manager",
                "department_code": "LOG"
            },
            {
                "email": "hr@hemrajgroup.com",
                "full_name": "HR Manager",
                "password": "HR@HIPL2026",
                "role_name": "HR Manager",
                "department_code": "HR"
            },
            {
                "email": "quality@hemrajgroup.com",
                "full_name": "Quality Manager",
                "password": "Quality@HIPL2026",
                "role_name": "Quality Manager",
                "department_code": "QA"
            },
            {
                "email": "sales@hemrajgroup.com",
                "full_name": "Sales Manager",
                "password": "Sales@HIPL2026",
                "role_name": "Sales Manager",
                "department_code": "SAL"
            },
            {
                "email": "compliance@hemrajgroup.com",
                "full_name": "Compliance Officer",
                "password": "Compliance@HIPL2026",
                "role_name": "Compliance Officer",
                "department_code": "COMP"
            },
        ]
        
        for user_data in users_data:
            password = user_data.pop("password")
            role_name = user_data.pop("role_name")
            department_code = user_data.pop("department_code", None)
            
            user = User(
                **user_data,
                hashed_password=get_password_hash(password),
                department_id=departments[department_code].id if department_code else None
            )
            user.roles.append(roles[role_name])
            db.add(user)
        
        db.commit()
        logger.info("✅ Users created successfully")
        logger.info("🌱 Database seeding completed!")
        
    except Exception as e:
        db.rollback()
        logger.error(f"❌ Database seeding failed: {str(e)}")
        raise
    finally:
        db.close()


def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
