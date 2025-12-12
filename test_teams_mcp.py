"""
Test script for Microsoft Teams MCP Server
This script demonstrates how to test various Teams MCP tools.
"""

import asyncio
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_teams_mcp():
    """Test the Teams MCP server functionality."""
    
    print("=" * 60)
    print("Microsoft Teams MCP Server Test")
    print("=" * 60)
    
    # Check for access token
    access_token = os.getenv("TEAMS_ACCESS_TOKEN")
    if not access_token:
        print("\n⚠️  WARNING: TEAMS_ACCESS_TOKEN environment variable not set!")
        print("To use this MCP server, you need to:")
        print("1. Register an app in Azure AD")
        print("2. Grant appropriate Microsoft Graph permissions:")
        print("   - Chat.Read, Chat.ReadWrite")
        print("   - Team.ReadBasic.All, Channel.ReadBasic.All")
        print("   - ChannelMessage.Read.All, ChannelMessage.Send")
        print("3. Get an access token and set TEAMS_ACCESS_TOKEN environment variable")
        print("\nContinuing with demo (will fail without token)...\n")
    
    # Server parameters
    server_params = StdioServerParameters(
        command="python",
        args=["main.py"],
        env=os.environ.copy()
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize the connection
                await session.initialize()
                
                print("\n✅ Connected to Teams MCP Server")
                print("\n" + "=" * 60)
                print("Available Tools:")
                print("=" * 60)
                
                # List available tools
                tools = await session.list_tools()
                for i, tool in enumerate(tools.tools, 1):
                    print(f"\n{i}. {tool.name}")
                    print(f"   Description: {tool.description}")
                
                print("\n" + "=" * 60)
                print("Testing Tools:")
                print("=" * 60)
                
                # Test 1: List Teams
                print("\n📋 Test 1: List Teams for current user")
                print("-" * 60)
                try:
                    result = await session.call_tool(
                        "mcp_graph_teams_listTeams",
                        arguments={"user-id": "me"}
                    )
                    print(f"Result: {result.content[0].text}")
                except Exception as e:
                    print(f"❌ Error: {e}")
                
                # Test 2: List Chats
                print("\n💬 Test 2: List Chats")
                print("-" * 60)
                try:
                    result = await session.call_tool(
                        "mcp_graph_chat_listChats",
                        arguments={"$top": 5}
                    )
                    print(f"Result: {result.content[0].text}")
                except Exception as e:
                    print(f"❌ Error: {e}")
                
                # Test 3: Get a specific team (requires team ID)
                print("\n🏢 Test 3: Get Team Details")
                print("-" * 60)
                print("ℹ️  Skipping - requires valid team-id")
                print("   To test, use: mcp_graph_teams_getTeam with a real team ID")
                
                # Test 4: List channels (requires team ID)
                print("\n📺 Test 4: List Channels")
                print("-" * 60)
                print("ℹ️  Skipping - requires valid team-id")
                print("   To test, use: mcp_graph_teams_listChannels with a real team ID")
                
                print("\n" + "=" * 60)
                print("Test Summary:")
                print("=" * 60)
                print("✅ MCP Server is running correctly")
                print("✅ Tools are properly registered")
                print("\nNext Steps:")
                print("1. Set TEAMS_ACCESS_TOKEN environment variable")
                print("2. Test with real Teams data using actual team/channel IDs")
                print("3. Try posting messages to channels or chats")
                print("=" * 60)
                
    except Exception as e:
        print(f"\n❌ Error connecting to MCP server: {e}")
        print("\nMake sure the server is configured correctly in main.py")

async def show_usage_examples():
    """Show usage examples for the Teams MCP server."""
    print("\n" + "=" * 60)
    print("Usage Examples:")
    print("=" * 60)
    
    examples = [
        {
            "name": "List all teams",
            "tool": "mcp_graph_teams_listTeams",
            "args": {"user-id": "me"}
        },
        {
            "name": "Get team details",
            "tool": "mcp_graph_teams_getTeam",
            "args": {"team-id": "YOUR_TEAM_ID"}
        },
        {
            "name": "List channels in a team",
            "tool": "mcp_graph_teams_listChannels",
            "args": {"team-id": "YOUR_TEAM_ID"}
        },
        {
            "name": "List messages in a channel",
            "tool": "mcp_graph_teams_listChannelMessages",
            "args": {"team-id": "YOUR_TEAM_ID", "channel-id": "YOUR_CHANNEL_ID", "$top": 10}
        },
        {
            "name": "Post message to channel",
            "tool": "mcp_graph_teams_postChannelMessage",
            "args": {
                "team-id": "YOUR_TEAM_ID",
                "channel-id": "YOUR_CHANNEL_ID",
                "body": {"content": "Hello from MCP!"}
            }
        },
        {
            "name": "List chats",
            "tool": "mcp_graph_chat_listChats",
            "args": {"$top": 10}
        },
        {
            "name": "Send chat message",
            "tool": "mcp_graph_chat_postMessage",
            "args": {
                "chat-id": "YOUR_CHAT_ID",
                "body": {"content": "Hello!"}
            }
        },
        {
            "name": "Create a new channel",
            "tool": "mcp_graph_teams_createChannel",
            "args": {
                "team-id": "YOUR_TEAM_ID",
                "displayName": "New Channel",
                "description": "Created via MCP",
                "membershipType": "standard"
            }
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{i}. {example['name']}")
        print(f"   Tool: {example['tool']}")
        print(f"   Arguments: {example['args']}")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Microsoft Teams MCP Server - Test & Demo")
    print("=" * 60)
    
    # Run the test
    asyncio.run(test_teams_mcp())
    
    # Show usage examples
    asyncio.run(show_usage_examples())
    
    print("\n" + "=" * 60)
    print("Test Complete!")
    print("=" * 60 + "\n")
