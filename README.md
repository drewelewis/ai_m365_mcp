

## Microsoft Teams MCP Server

This repository contains a Model Context Protocol (MCP) server for interacting with Microsoft Teams via the Microsoft Graph API.

### Features

- **Chat Management**: Create, read, update, and delete Teams chats
- **Message Operations**: Send, retrieve, edit, and delete messages
- **Channel Management**: Create and manage Teams channels
- **Team Operations**: List and retrieve team information
- **Member Management**: Add and manage team/channel members

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

4. **Run the server**:
   ```cmd
   python main.py
   ```

5. **Test the server**:
   ```cmd
   python test_teams_mcp.py
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
