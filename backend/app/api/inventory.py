"""Inventory & Warehouse Management Endpoints"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.dependencies import check_permission
from app.models.user import User

router = APIRouter()


@router.get("/stock")
async def get_stock(
    current_user: User = Depends(check_permission(required_roles=["Inventory Manager"])),
    db: Session = Depends(get_db)
):
    """Get real-time stock levels - Inventory Dashboard"""
    return {
        "message": "Stock endpoint",
        "user": current_user.email
    }


@router.post("/grn")
async def create_grn(
    current_user: User = Depends(check_permission(required_roles=["Inventory Manager"])),
    db: Session = Depends(get_db)
):
    """Create Goods Receipt Note"""
    return {"message": "GRN creation endpoint"}


@router.get("/batches")
async def get_batches(
    current_user: User = Depends(check_permission(required_roles=["Inventory Manager"])),
    db: Session = Depends(get_db)
):
    """Get batch tracking information"""
    return {"message": "Batches endpoint"}
