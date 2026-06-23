"""Application Configuration"""

from pydantic_settings import BaseSettings
from typing import List
from functools import lru_cache
import os


class Settings(BaseSettings):
    """Application Settings"""
    
    # App Settings
    APP_NAME: str = "Project HIPL"
    APP_ENV: str = os.getenv("APP_ENV", "development")
    APP_DEBUG: bool = os.getenv("APP_DEBUG", "true").lower() == "true"
    APP_PORT: int = 8000
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://hipl_user:HIPL_SecurePass2026@localhost:3306/hipl_db"
    )
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: int = int(os.getenv("DATABASE_PORT", "3306"))
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "hipl_db")
    DATABASE_USER: str = os.getenv("DATABASE_USER", "hipl_user")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "HIPL_SecurePass2026")
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 40
    
    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", "6379"))
    
    # JWT
    JWT_SECRET_KEY: str = os.getenv(
        "JWT_SECRET_KEY",
        "your-super-secret-jwt-key-change-this-in-production-minimum-32-characters"
    )
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    JWT_REFRESH_EXPIRATION_DAYS: int = 7
    
    # N8N
    N8N_URL: str = os.getenv("N8N_URL", "http://localhost:5678")
    N8N_API_KEY: str = os.getenv("N8N_API_KEY", "")
    N8N_WEBHOOK_URL: str = os.getenv("N8N_WEBHOOK_URL", "http://localhost:5678/webhook")
    
    # Email
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USERNAME: str = os.getenv("SMTP_USERNAME", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    SMTP_FROM_EMAIL: str = os.getenv("SMTP_FROM_EMAIL", "noreply@hemrajgroup.com")
    SMTP_FROM_NAME: str = os.getenv("SMTP_FROM_NAME", "Hemraj Group - HIPL")
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8000",
        "http://127.0.0.1",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    
    # Security
    SECURE_COOKIES: bool = False
    HTTPS_ONLY: bool = False
    
    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT: str = "json"
    LOG_FILE: str = "logs/app.log"
    
    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_REQUESTS: int = 1000
    RATE_LIMIT_PERIOD: int = 60  # seconds
    
    # File Upload
    UPLOAD_PATH: str = "uploads"
    MAX_UPLOAD_SIZE: int = 52428800  # 50MB
    EXCEL_UPLOAD_PATH: str = "uploads/excel"
    EXCEL_MAX_FILE_SIZE: int = 10485760  # 10MB
    
    # Features
    ENABLE_AUDIT_LOGGING: bool = True
    ENABLE_REAL_TIME_UPDATES: bool = True
    ENABLE_WORKFLOW_MONITORING: bool = True
    
    # Timezone
    TIMEZONE: str = "Asia/Kolkata"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get application settings (cached)"""
    return Settings()


settings = get_settings()
