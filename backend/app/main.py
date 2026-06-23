"""Main FastAPI Application Entry Point"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager
import logging
from datetime import datetime

from app.config import settings
from app.database.database import init_db, get_db
from app.api import auth, accounting, procurement, production, inventory, logistics, hr, quality, sales, compliance
from app.middleware.error_handler import global_exception_handler
from app.middleware.request_logger import RequestLoggingMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for FastAPI app startup and shutdown"""
    # Startup
    logger.info("🚀 Starting Project HIPL - N8N Automation Platform")
    logger.info(f"📅 Started at: {datetime.now().isoformat()}")
    logger.info(f"🌍 Environment: {settings.APP_ENV}")
    
    # Initialize database
    try:
        init_db()
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {str(e)}")
    
    yield
    
    # Shutdown
    logger.info("🛑 Shutting down Project HIPL")
    logger.info(f"📅 Shutdown at: {datetime.now().isoformat()}")


# Create FastAPI app
app = FastAPI(
    title="Project HIPL - N8N Automation Platform",
    description="Enterprise-grade automation solution for Hemraj Group's manufacturing operations",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Trusted Host Middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=settings.ALLOWED_HOSTS,
)

# Request Logging Middleware
app.add_middleware(RequestLoggingMiddleware)


# Health Check Endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "Project HIPL",
        "version": "1.0.0"
    }


# Root Endpoint
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to Project HIPL - N8N Automation Platform",
        "company": "Hemraj Group",
        "version": "1.0.0",
        "documentation": "Available at /docs",
        "health_check": "/health",
        "api_version": "v1",
        "base_url": "/api/v1"
    }


# API v1 Routes
app.include_router(
    auth.router,
    prefix="/api/v1/auth",
    tags=["Authentication"]
)

app.include_router(
    accounting.router,
    prefix="/api/v1/accounting",
    tags=["Accounting & Finance"]
)

app.include_router(
    procurement.router,
    prefix="/api/v1/procurement",
    tags=["Procurement & Vendor Management"]
)

app.include_router(
    production.router,
    prefix="/api/v1/production",
    tags=["Production & Operations"]
)

app.include_router(
    inventory.router,
    prefix="/api/v1/inventory",
    tags=["Inventory & Warehouse"]
)

app.include_router(
    logistics.router,
    prefix="/api/v1/logistics",
    tags=["Logistics & Supply Chain"]
)

app.include_router(
    hr.router,
    prefix="/api/v1/hr",
    tags=["HR & Administration"]
)

app.include_router(
    quality.router,
    prefix="/api/v1/quality",
    tags=["Quality Control"]
)

app.include_router(
    sales.router,
    prefix="/api/v1/sales",
    tags=["Sales & Customer Management"]
)

app.include_router(
    compliance.router,
    prefix="/api/v1/compliance",
    tags=["Compliance & Legal"]
)


# Global Exception Handler
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Global exception handler"""
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "error": str(exc) if settings.APP_DEBUG else "An error occurred"
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
