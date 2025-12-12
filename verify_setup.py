"""
Simple verification script to check MCP server configuration
This script checks if the server is properly configured without requiring authentication.
"""

import sys
import os

def check_file_exists(filepath, description):
    """Check if a file exists."""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description} not found: {filepath}")
        return False

def check_imports():
    """Check if required packages are installed."""
    print("\nChecking Python packages...")
    packages = {
        'mcp': 'Model Context Protocol',
        'httpx': 'HTTP client library',
        'fastapi': 'FastAPI framework',
        'pydantic_settings': 'Pydantic Settings',
        'dotenv': 'Python dotenv'
    }
    
    all_installed = True
    for package, description in packages.items():
        try:
            __import__(package)
            print(f"✅ {description} ({package})")
        except ImportError:
            print(f"❌ {description} ({package}) - NOT INSTALLED")
            all_installed = False
    
    return all_installed

def check_server_structure():
    """Check if the server module is properly structured."""
    print("\nChecking server structure...")
    try:
        sys.path.insert(0, os.getcwd())
        from app.server import mcp
        print("✅ Server module loaded successfully")
        
        # Check if mcp is a Server instance
        if hasattr(mcp, 'name'):
            print(f"✅ MCP Server name: {mcp.name}")
        
        return True
    except Exception as e:
        print(f"❌ Error loading server module: {e}")
        return False

def main():
    print("=" * 60)
    print("Microsoft Teams MCP Server - Configuration Verification")
    print("=" * 60)
    
    # Check files
    print("\nChecking required files...")
    files_ok = all([
        check_file_exists("app/server.py", "Server module"),
        check_file_exists("main.py", "Main entry point"),
        check_file_exists("requirements.txt", "Requirements file"),
        check_file_exists("test_teams_mcp.py", "Test script"),
        check_file_exists("TEAMS_MCP_SETUP.md", "Setup documentation")
    ])
    
    # Check packages
    packages_ok = check_imports()
    
    # Check server
    server_ok = check_server_structure()
    
    # Summary
    print("\n" + "=" * 60)
    print("Verification Summary:")
    print("=" * 60)
    
    if files_ok and packages_ok and server_ok:
        print("✅ All checks passed!")
        print("\nNext steps:")
        print("1. Get an access token (run: python get_token.py)")
        print("2. Set TEAMS_ACCESS_TOKEN environment variable")
        print("3. Test the server (run: python test_teams_mcp.py)")
        print("4. Start the server (run: python main.py)")
    else:
        print("❌ Some checks failed!")
        if not files_ok:
            print("   - Missing required files")
        if not packages_ok:
            print("   - Missing required packages (run: pip install -r requirements.txt)")
        if not server_ok:
            print("   - Server configuration issue")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
