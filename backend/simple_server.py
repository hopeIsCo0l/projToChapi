from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
import os
from datetime import datetime

app = FastAPI(
    title="Waitlist API",
    description="A simple waitlist management system",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple in-memory storage
WAITLIST_FILE = "waitlist_data.json"
ADMIN_PASSWORD = "admin123"

class WaitlistEntry(BaseModel):
    email: str

class WaitlistResponse(BaseModel):
    entries: List[dict]
    total: int

def load_waitlist():
    if os.path.exists(WAITLIST_FILE):
        with open(WAITLIST_FILE, 'r') as f:
            return json.load(f)
    return []

def save_waitlist(data):
    with open(WAITLIST_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.get("/")
async def root():
    return {"message": "Waitlist API is running!", "status": "ok", "service": "waitlist-backend"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "waitlist-backend"}

@app.post("/api/v1/waitlist/signup")
async def signup_waitlist(entry: WaitlistEntry):
    waitlist = load_waitlist()
    
    # Check if email already exists
    for item in waitlist:
        if item['email'] == entry.email:
            return {"message": "Email already registered", "success": False}
    
    # Add new entry
    new_entry = {
        "id": len(waitlist) + 1,
        "email": entry.email,
        "signup_date": datetime.now().isoformat()
    }
    waitlist.append(new_entry)
    save_waitlist(waitlist)
    
    return {"message": "Successfully added to waitlist!", "success": True}

@app.get("/api/v1/admin/entries")
async def get_waitlist_entries():
    waitlist = load_waitlist()
    return WaitlistResponse(entries=waitlist, total=len(waitlist))

if __name__ == "__main__":
    import uvicorn
    import os
    
    # Get port from environment variable (Railway sets this)
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
