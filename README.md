# Microsoft 365 MCP Integration

A Python-based MCP (Model Context Protocol) client for interacting with Microsoft's M365 MCP servers. This repository demonstrates how to leverage Microsoft's Teams MCP server to programmatically manage Microsoft Teams resources through a standardized protocol interface.

## Purpose

This repository serves as a **learning and testing environment** for developers who want to:

1. **Understand MCP Architecture**: Learn how to build MCP clients that connect to Microsoft's hosted MCP servers
2. **Explore M365 Integration**: Discover the capabilities of Microsoft's Teams MCP server without building from scratch
3. **Prototype Teams Automation**: Quickly test and validate Teams automation scenarios using MCP tools
4. **Bridge AI and Teams**: Create AI-powered applications that can interact with Microsoft Teams through a standardized protocol

### What is MCP?

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io) is an open standard that enables AI applications to securely connect to data sources and tools. Microsoft has implemented MCP servers for their M365 services, allowing developers to interact with Teams, Outlook, and other M365 services through a consistent protocol.

**Key benefits of using MCP:**
- **Standardized Interface**: Consistent way to interact with different services
- **AI-Ready**: Designed for integration with AI assistants and agents
- **Tool Discovery**: Automatically discover available operations and their schemas
- **Security**: Built-in authentication and authorization patterns

## What This Repository Does

This is a **MCP client application** (not a server) that:
- ✅ Connects to Microsoft's hosted Teams MCP server
- ✅ Authenticates using Microsoft Graph API tokens
- ✅ Provides test scripts to explore available MCP tools
- ✅ Demonstrates real-world usage patterns for Teams automation
- ✅ Includes helper utilities for token management and setup verification

**What it does NOT do:**
- ❌ Implement a custom MCP server
- ❌ Replace the Microsoft Graph API (it uses Graph API for auth)
- ❌ Require you to host any infrastructure

### What You Can Do

- **Chat Management**: Create, read, update, and delete Teams chats
- **Message Operations**: Send, retrieve, edit, and delete messages
- **Channel Management**: Create and manage Teams channels
- **Team Operations**: List and retrieve team information
- **Member Management**: Add and manage team/channel members

## Repository Structure

```
ai_m365_mcp/
├── test_teams_mcp.py          # Main test script for Teams MCP tools
├── get_token.py               # Helper to obtain Microsoft Graph tokens
├── verify_setup.py            # Setup verification script
├── requirements.txt           # Python dependencies
├── .env                       # Environment configuration (not committed)
├── setup_teams_mcp.bat        # Windows setup automation
└── README.md                  # This file
```

## Use Cases

This MCP client is ideal for:

- **AI Agent Development**: Building AI assistants that need to interact with Microsoft Teams
- **Workflow Automation**: Creating automated workflows for Teams management
- **Integration Testing**: Validating integration patterns before production deployment
- **Learning MCP**: Understanding how to work with MCP protocol and Microsoft's implementation
- **Rapid Prototyping**: Quickly testing Teams automation ideas without complex setup

### Quick Start

1. **Install dependencies**:
   ```cmd
   pip install -r requirements.txt
   ```

2. **Configure environment variables**:
   
   Update the `.env` file with your credentials:
   ```env
   # Microsoft Teams MCP Server Configuration
   TEAMS_ACCESS_TOKEN=your_access_token_here
   
   # Optional: Azure AD App Configuration (for automated token refresh)
   # AZURE_TENANT_ID=your-tenant-id-here
   # AZURE_CLIENT_ID=your-client-id-here
   # AZURE_CLIENT_SECRET=your-client-secret-here
   ```

3. **Get an access token**:
   
   **Option 1 - Using Azure CLI (recommended):**
   ```cmd
   python get_token.py
   ```
   This script will automatically get the token and offer to save it to `.env`
   
   **Option 2 - Manual via Azure CLI:**
   ```cmd
   az login
   az account get-access-token --resource https://graph.microsoft.com --query accessToken -o tsv
   ```
   Copy the token and add it to `.env` file: `TEAMS_ACCESS_TOKEN=<your_token>`

4. **Test the MCP client**:
   ```cmd
   python test_teams_mcp.py
   ```
   This will connect to Microsoft's Teams MCP server and demonstrate available tools.

5. **Verify your setup** (optional):
   ```cmd
   python verify_setup.py
   ```

---

## Setup Guide

### Prerequisites

1. **Azure AD App Registration** (required for production or app-only access)
### Chat Operations
- `mcp_graph_chat_listChats` - List all chats
- `mcp_graph_chat_getChat` - Get specific chat details
- `mcp_graph_chat_createChat` - Create a new chat
- `mcp_graph_chat_postMessage` - Send a message to a chat
- `mcp_graph_chat_listChatMessages` - List messages in a chat
- `mcp_graph_chat_updateChat` - Update chat properties
- `mcp_graph_chat_deleteChat` - Delete a chat
- `mcp_graph_chat_listChatMembers` - List chat members
- `mcp_graph_chat_addChatMember` - Add member to chat

### Team & Channel Operations
- `mcp_graph_teams_listTeams` - List user's joined teams
- `mcp_graph_teams_getTeam` - Get team details
- `mcp_graph_teams_listChannels` - List channels in a team
- `mcp_graph_teams_getChannel` - Get channel details
- `mcp_graph_teams_createChannel` - Create a new channel
- `mcp_graph_teams_postChannelMessage` - Post message to a channel
- `mcp_graph_teams_listChannelMessages` - List messages in a channel
- `mcp_graph_teams_replyToChannelMessage` - Reply to a channel message
- `mcp_graph_teams_listChannelMembers` - List channel members
- `mcp_graph_teams_addChannelMember` - Add member to channel

---

## Usage Examples

### List All Teams
```python
result = await session.call_tool(
    "mcp_graph_teams_listTeams",
    arguments={"user-id": "me"}
)
```

### Post Message to Channel
```python
result = await session.call_tool(
    "mcp_graph_teams_postChannelMessage",
    arguments={
        "team-id": "your-team-id",
        "channel-id": "your-channel-id",
        "body": {"content": "Hello from MCP!"}
    }
)
```

### List Recent Chats
```python
result = await session.call_tool(
    "mcp_graph_chat_listChats",
    arguments={"$top": 10, "$orderby": "lastMessagePreview/createdDateTime desc"}
)
```

### Create a New Channel
```python
result = await session.call_tool(
    "mcp_graph_teams_createChannel",
    arguments={
        "team-id": "your-team-id",
        "displayName": "Project Updates",
        "description": "Channel for project status updates",
        "membershipType": "standard"
    }
)
```

---
   - `Team.ReadBasic.All` - Read basic team information
   - `Channel.ReadBasic.All` - Read basic channel information
   - `ChannelMessage.Read.All` - Read channel messages
   - `ChannelMessage.Send` - Send channel messages
   - `TeamMember.Read.All` - Read team members

3. **Configure API Permissions in Azure AD**
   - In your app registration, go to **API permissions**
   - Click **Add a permission** > **Microsoft Graph** > **Delegated permissions**
   - Add the permissions listed above
   - Click **Grant admin consent** (requires admin privileges)

### Getting an Access Token

**For Development/Testing (Easiest):**

Using Azure CLI:
```cmd
az login
python get_token.py
```
The script will automatically save the token to `.env`

**For Production (App-Only Access):**

1. In Azure Portal, go to **Certificates & secrets**
2. Create a new client secret
3. Add these to `.env`:
   ```env
   AZURE_TENANT_ID=your_tenant_id
   AZURE_CLIENT_ID=your_client_id
   AZURE_CLIENT_SECRET=your_client_secret
   ```

---

## Available Tools

#### Chat Tools
- `mcp_graph_chat_listChats` - List all chats
- `mcp_graph_chat_getChat` - Get specific chat
- `mcp_graph_chat_createChat` - Create new chat
- `mcp_graph_chat_postMessage` - Send message to chat
**Permission errors (403 Forbidden):**
Ensure your Azure AD app has the required Microsoft Graph permissions:
- Chat.Read, Chat.ReadWrite
- Team.ReadBasic.All, Channel.ReadBasic.All
- ChannelMessage.Read.All, ChannelMessage.Send

**Resource not found (404):**
- Verify that team-id and channel-id are correct
- Use `listTeams` and `listChannels` to find valid IDs
- Ensure the user has access to the specified resources

---

## References

- [Microsoft Teams MCP Server Reference](https://learn.microsoft.com/en-us/microsoft-agent-365/mcp-server-reference/teams)
- [Microsoft Graph API Documentation](https://learn.microsoft.com/en-us/graph/overview)
- [Azure AD App Registration Guide](https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app)
- `mcp_graph_teams_listChannels` - List team channels
- `mcp_graph_teams_createChannel` - Create new channel
- `mcp_graph_teams_postChannelMessage` - Post to channel
- `mcp_graph_teams_listChannelMessages` - List channel messages

### Requirements

- Python 3.8+
- Azure AD app registration with Microsoft Graph permissions
- Valid access token for Microsoft Graph API

### Environment Configuration

The project uses a `.env` file for configuration. Key settings include:

**Teams MCP Server:**
- `TEAMS_ACCESS_TOKEN` - Microsoft Graph API access token (required)
- `AZURE_TENANT_ID` - Your Azure AD tenant ID (optional, for automated auth)
- `AZURE_CLIENT_ID` - Your Azure AD app client ID (optional)
- `AZURE_CLIENT_SECRET` - Your Azure AD app secret (optional)

**Database (optional, for other features):**
- `DATABASE_URL` - PostgreSQL connection string
- `DB_FORCE_ROLLBACK` - Force rollback transactions (true/false)

**OpenAI/Azure OpenAI (optional, for AI features):**
- `OPENAI_API_BASE` - Azure OpenAI endpoint
- `OPENAI_API_KEY` - Azure OpenAI API key
- `OPENAI_API_VERSION` - API version
- `OPENAI_API_MODEL_DEPLOYMENT_NAME` - Model deployment name

### Security

⚠️ **Never commit access tokens to version control!** 

- The `.env` file is already added to `.gitignore`
- Access tokens typically expire after 1 hour
- Refresh tokens using `python get_token.py`
- For production, use Azure AD app credentials for automatic token refresh

### Troubleshooting

**Token expired (401 Unauthorized):**
```cmd
python get_token.py
```

**Azure CLI not found:**
Install from: https://docs.microsoft.com/cli/azure/install-azure-cli

**Permission errors (403 Forbidden):**
Ensure your Azure AD app has the required Microsoft Graph permissions:
- Chat.Read, Chat.ReadWrite
- Team.ReadBasic.All, Channel.ReadBasic.All
- ChannelMessage.Read.All, ChannelMessage.Send
