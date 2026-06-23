"""HR & Administration Endpoints"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.dependencies import check_permission
from app.models.user import User

router = APIRouter()


@router.get("/employees")
async def get_employees(
    current_user: User = Depends(check_permission(required_roles=["HR Manager"])),
    db: Session = Depends(get_db)
):
    """Get employee information - HR Dashboard"""
    return {
        "message": "Employees endpoint",
        "user": current_user.email
    }


@router.post("/onboarding")
async def create_onboarding(
    current_user: User = Depends(check_permission(required_roles=["HR Manager"])),
    db: Session = Depends(get_db)
):
    """Create employee onboarding workflow"""
    return {"message": "Onboarding endpoint"}


@router.get("/attendance")
async def get_attendance(
    current_user: User = Depends(check_permission(required_roles=["HR Manager"])),
    db: Session = Depends(get_db)
):
    """Get attendance records"""
    return {"message": "Attendance endpoint"}
