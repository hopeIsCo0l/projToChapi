from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List

class WaitlistSignupRequest(BaseModel):
    email: EmailStr

class WaitlistSignupResponse(BaseModel):
    message: str
    success: bool

class WaitlistEntryResponse(BaseModel):
    id: int
    email: str
    signup_date: datetime
    
    class Config:
        from_attributes = True

class WaitlistEntriesResponse(BaseModel):
    entries: List[WaitlistEntryResponse]
    total: int

