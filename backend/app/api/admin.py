from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from sqlalchemy import desc
from ..database import get_db
from ..models import WaitlistEntry
from ..schemas import WaitlistEntriesResponse, WaitlistEntryResponse
import os
import secrets

router = APIRouter()
security = HTTPBasic()

def get_admin_password():
    return os.getenv("ADMIN_PASSWORD", "admin123")

def verify_admin(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Verify admin credentials using HTTP Basic Auth.
    """
    correct_password = get_admin_password()
    is_correct_password = secrets.compare_digest(
        credentials.password, correct_password
    )
    
    if not is_correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect admin password",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    return credentials.username

@router.get("/entries", response_model=WaitlistEntriesResponse)
async def get_waitlist_entries(
    db: Session = Depends(get_db),
    admin: str = Depends(verify_admin)
):
    """
    Get all waitlist entries (admin only).
    Returns entries sorted by signup date (newest first).
    """
    try:
        entries = db.query(WaitlistEntry).order_by(desc(WaitlistEntry.signup_date)).all()
        
        entry_responses = [
            WaitlistEntryResponse(
                id=entry.id,
                email=entry.email,
                signup_date=entry.signup_date
            )
            for entry in entries
        ]
        
        return WaitlistEntriesResponse(
            entries=entry_responses,
            total=len(entry_responses)
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )


