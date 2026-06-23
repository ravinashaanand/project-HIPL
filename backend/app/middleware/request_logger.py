"""Request Logging Middleware"""

from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import logging
import time
from datetime import datetime

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware to log all incoming requests and responses
    """
    
    async def dispatch(self, request: Request, call_next):
        # Start time
        start_time = time.time()
        
        # Log request
        logger.info(
            f"📨 Request: {request.method} {request.url.path}",
            extra={
                "method": request.method,
                "path": request.url.path,
                "client": request.client,
                "timestamp": datetime.utcnow().isoformat()
            }
        )
        
        # Process request
        response = await call_next(request)
        
        # Calculate duration
        duration = time.time() - start_time
        
        # Log response
        logger.info(
            f"📤 Response: {response.status_code} - {request.method} {request.url.path} ({duration:.2f}s)",
            extra={
                "status_code": response.status_code,
                "duration": duration,
                "path": request.url.path
            }
        )
        
        return response
