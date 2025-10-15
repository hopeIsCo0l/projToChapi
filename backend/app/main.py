from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import waitlist, admin
from .database import engine
from .models import Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Waitlist API",
    description="A simple waitlist management system with admin dashboard",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-frontend-domain.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Waitlist API is running!"}

# Include API routers
app.include_router(waitlist.router, prefix="/api/v1/waitlist", tags=["waitlist"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["admin"])

