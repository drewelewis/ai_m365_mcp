@echo off
REM Microsoft Teams MCP Server - Quick Setup Script

echo ======================================================
echo Microsoft Teams MCP Server - Setup
echo ======================================================
echo.

echo Step 1: Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ======================================================
echo Step 2: Getting access token...
echo ======================================================
echo.
echo You have two options to get an access token:
echo.
echo Option 1: Use Azure CLI (recommended)
echo   Run: python get_token.py
echo.
echo Option 2: Manual setup
echo   See TEAMS_MCP_SETUP.md for instructions
echo.

set /p GET_TOKEN="Do you want to run get_token.py now? (y/n): "
if /i "%GET_TOKEN%"=="y" (
    python get_token.py
)

echo.
echo ======================================================
echo Step 3: Set Environment Variable
echo ======================================================
echo.
echo If you haven't already, set the TEAMS_ACCESS_TOKEN:
echo   set TEAMS_ACCESS_TOKEN=your_token_here
echo.
echo Or add to .env file:
echo   TEAMS_ACCESS_TOKEN=your_token_here
echo.

pause

echo.
echo ======================================================
echo Step 4: Test the server
echo ======================================================
echo.

set /p RUN_TEST="Do you want to run the test now? (y/n): "
if /i "%RUN_TEST%"=="y" (
    python test_teams_mcp.py
)

echo.
echo ======================================================
echo Setup Complete!
echo ======================================================
echo.
echo To start the MCP server, run:
echo   python main.py
echo.
echo To test the server, run:
echo   python test_teams_mcp.py
echo.
echo For more information, see TEAMS_MCP_SETUP.md
echo ======================================================

pause
