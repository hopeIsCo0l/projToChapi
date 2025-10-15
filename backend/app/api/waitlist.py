from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import WaitlistEntry
from ..schemas import WaitlistSignupRequest, WaitlistSignupResponse
from ..email_service import send_confirmation_email
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/signup", response_model=WaitlistSignupResponse)
async def signup_waitlist(
    request: WaitlistSignupRequest,
    db: Session = Depends(get_db)
):
    """
    Add a new email to the waitlist.
    """
    try:
        # Check if email already exists
        existing_entry = db.query(WaitlistEntry).filter(
            WaitlistEntry.email == request.email
        ).first()
        
        if existing_entry:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists in waitlist"
            )
        
        # Create new waitlist entry
        new_entry = WaitlistEntry(email=request.email)
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        
        # Send confirmation email
        email_sent = send_confirmation_email(request.email)
        
        logger.info(f"New waitlist signup: {request.email}")
        
        return WaitlistSignupResponse(
            message="Successfully added to waitlist!",
            success=True
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error adding to waitlist: {e}")
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )


