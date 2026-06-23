"""Quality Control & Assurance Endpoints"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.dependencies import check_permission
from app.models.user import User

router = APIRouter()


@router.get("/checks")
async def get_quality_checks(
    current_user: User = Depends(check_permission(required_roles=["Quality Manager"])),
    db: Session = Depends(get_db)
):
    """Get quality control checks - Quality Dashboard"""
    return {
        "message": "Quality checks endpoint",
        "user": current_user.email
    }


@router.post("/non-conformance")
async def create_non_conformance(
    current_user: User = Depends(check_permission(required_roles=["Quality Manager"])),
    db: Session = Depends(get_db)
):
    """Create non-conformance report"""
    return {"message": "Non-conformance endpoint"}


@router.get("/audits")
async def get_audits(
    current_user: User = Depends(check_permission(required_roles=["Quality Manager"])),
    db: Session = Depends(get_db)
):
    """Get audit information"""
    return {"message": "Audits endpoint"}
