#!/usr/bin/env python3
"""
Railway-compatible server startup script
"""
import os
import uvicorn

if __name__ == "__main__":
    # Get port from environment variable (Railway sets this)
    port = int(os.environ.get("PORT", 8000))
    
    # Start the server
    uvicorn.run(
        "simple_server:app",
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
