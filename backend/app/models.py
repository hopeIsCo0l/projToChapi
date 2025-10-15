from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.sql import func
from .database import Base

class WaitlistEntry(Base):
    __tablename__ = "waitlist_entries"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    signup_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Create index on email for faster lookups
    __table_args__ = (
        Index('idx_email', 'email'),
    )

