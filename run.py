#!/usr/bin/env python3
"""
AuraSense Startup Script
Run this script to start the application locally
"""

import sys
import os

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    return True

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'flask',
        'cv2',
        'numpy',
        'librosa',
        'deepface',
        'pydub'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("Missing required packages:")
        for pkg in missing_packages:
            print(f"  - {pkg}")
        print("\nInstall with: pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Main startup function"""
    print("=== AuraSense Mental Health Detection System ===")
    print("Starting application...\n")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Start Flask app
    try:
        print("All checks passed. Starting Flask application...")
        print("Application will be available at: http://localhost:5000")
        print("Press Ctrl+C to stop the application\n")
        
        # Import and run the app
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except KeyboardInterrupt:
        print("\nApplication stopped by user")
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
