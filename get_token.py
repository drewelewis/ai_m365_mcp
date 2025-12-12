"""
Helper script to get Microsoft Graph access token for Teams MCP Server.
This script uses the Azure CLI to obtain an access token.
"""

import subprocess
import sys
import os

def get_access_token_via_azure_cli():
    """Get access token using Azure CLI."""
    print("Getting access token via Azure CLI...")
    print("Make sure you're logged in with: az login\n")
    
    try:
        # Run Azure CLI command to get access token
        result = subprocess.run(
            [
                "az", "account", "get-access-token",
                "--resource", "https://graph.microsoft.com",
                "--query", "accessToken",
                "-o", "tsv"
            ],
            capture_output=True,
            text=True,
            check=True
        )
        
        token = result.stdout.strip()
        if token:
            print("✅ Successfully obtained access token!\n")
            print("Token (first 20 chars):", token[:20] + "...")
            print("\nTo use this token, set the environment variable:")
            print("\nWindows (cmd):")
            print(f'set TEAMS_ACCESS_TOKEN={token}')
            print("\nWindows (PowerShell):")
            print(f'$env:TEAMS_ACCESS_TOKEN="{token}"')
            print("\nLinux/Mac:")
            print(f'export TEAMS_ACCESS_TOKEN="{token}"')
            print("\nOr add to .env file:")
            print(f'TEAMS_ACCESS_TOKEN={token}')
            
            # Optionally save to .env file
            save = input("\nDo you want to save this to .env file? (y/n): ")
            if save.lower() == 'y':
                with open('.env', 'a') as f:
                    f.write(f'\nTEAMS_ACCESS_TOKEN={token}\n')
                print("✅ Saved to .env file!")
            
            return token
        else:
            print("❌ Failed to get access token")
            return None
            
    except subprocess.CalledProcessError as e:
        print("❌ Error running Azure CLI command:")
        print(e.stderr)
        print("\nMake sure:")
        print("1. Azure CLI is installed (https://docs.microsoft.com/cli/azure/install-azure-cli)")
        print("2. You are logged in (run: az login)")
        return None
    except FileNotFoundError:
        print("❌ Azure CLI not found!")
        print("\nPlease install Azure CLI:")
        print("https://docs.microsoft.com/cli/azure/install-azure-cli")
        return None

def check_azure_cli():
    """Check if Azure CLI is installed and user is logged in."""
    try:
        result = subprocess.run(
            ["az", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ Azure CLI is installed")
        print(result.stdout.split('\n')[0])
        
        # Check if logged in
        result = subprocess.run(
            ["az", "account", "show"],
            capture_output=True,
            text=True,
            check=True
        )
        print("✅ You are logged in to Azure\n")
        return True
        
    except subprocess.CalledProcessError:
        print("❌ Not logged in to Azure")
        print("Please run: az login")
        return False
    except FileNotFoundError:
        print("❌ Azure CLI not found")
        return False

def show_manual_instructions():
    """Show manual instructions for getting access token."""
    print("\n" + "=" * 60)
    print("Manual Access Token Setup")
    print("=" * 60)
    print("\nOption 1: Using Azure Portal")
    print("-" * 60)
    print("1. Go to https://portal.azure.com")
    print("2. Navigate to Azure Active Directory > App registrations")
    print("3. Create a new app registration")
    print("4. Go to API permissions > Add Microsoft Graph permissions")
    print("5. Add required permissions (see TEAMS_MCP_SETUP.md)")
    print("6. Go to Certificates & secrets > Create client secret")
    print("7. Use client credentials to get token")
    
    print("\nOption 2: Using Graph Explorer")
    print("-" * 60)
    print("1. Go to https://developer.microsoft.com/graph/graph-explorer")
    print("2. Sign in with your Microsoft account")
    print("3. Click 'Access token' in the left panel")
    print("4. Copy the token")
    
    print("\nOption 3: Using PowerShell")
    print("-" * 60)
    print("Install-Module -Name Microsoft.Graph -Scope CurrentUser")
    print("Connect-MgGraph -Scopes 'Chat.Read','Team.ReadBasic.All'")
    print("Get-MgContext | Select-Object -ExpandProperty Token")

if __name__ == "__main__":
    print("=" * 60)
    print("Microsoft Teams MCP Server - Access Token Helper")
    print("=" * 60)
    print()
    
    # Check if Azure CLI is available
    if check_azure_cli():
        token = get_access_token_via_azure_cli()
        if token:
            print("\n✅ Success! You can now run the Teams MCP server.")
        else:
            print("\n❌ Failed to get access token")
            show_manual_instructions()
    else:
        show_manual_instructions()
    
    print("\n" + "=" * 60)
    print("Next Steps:")
    print("=" * 60)
    print("1. Set the TEAMS_ACCESS_TOKEN environment variable")
    print("2. Run: python main.py (to start the server)")
    print("3. Run: python test_teams_mcp.py (to test the server)")
    print("=" * 60)
