"""Sales & Customer Management Endpoints"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.dependencies import check_permission
from app.models.user import User

router = APIRouter()


@router.get("/orders")
async def get_orders(
    current_user: User = Depends(check_permission(required_roles=["Sales Manager"])),
    db: Session = Depends(get_db)
):
    """Get sales orders - Sales Dashboard"""
    return {
        "message": "Orders endpoint",
        "user": current_user.email
    }


@router.post("/orders")
async def create_order(
    current_user: User = Depends(check_permission(required_roles=["Sales Manager"])),
    db: Session = Depends(get_db)
):
    """Create sales order"""
    return {"message": "Order creation endpoint"}


@router.get("/customers")
async def get_customers(
    current_user: User = Depends(check_permission(required_roles=["Sales Manager"])),
    db: Session = Depends(get_db)
):
    """Get customer information"""
    return {"message": "Customers endpoint"}
