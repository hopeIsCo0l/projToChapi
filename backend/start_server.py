#!/usr/bin/env python3
"""
Railway-compatible server startup script
"""
import os
import sys
import uvicorn

if __name__ == "__main__":
    # Get port from environment variable (Railway sets this)
    port_str = os.environ.get("PORT", "8000")
    try:
        port = int(port_str)
    except ValueError:
        print(f"Error: PORT environment variable '{port_str}' is not a valid integer")
        sys.exit(1)
    
    print(f"Starting server on port {port}")
    print(f"Environment: PORT={port_str}")
    
    # Start the server
    uvicorn.run(
        "simple_server:app",
        host="0.0.0.0",
        port=port,
        log_level="info",
        access_log=True
    )
