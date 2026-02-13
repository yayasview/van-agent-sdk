# Jordan Belfur — Tool Configuration

## MCP Servers

### HubSpot
- **Purpose:** Read and write deal records, contacts, and companies
- **MCP URL:** `https://mcp.hubspot.com/anthropic`
- **Auth:** Bearer token (stored in environment variable `HUBSPOT_MCP_TOKEN`)
- **Permissions:** Deals (read/write), Contacts (read/write), Companies (read)
- **Rules:**
  - Always confirm with team before writing any data
  - Never delete records
  - Never change deal stage without explicit instruction

### Clay (Future)
- **Purpose:** Account and contact enrichment
- **Integration:** API webhook (not MCP)
- **Auth:** API key (stored in environment variable `CLAY_API_KEY`)
- **Permissions:** Read-only enrichment queries

## Tool Access Boundaries

Jordan should NEVER be given access to:
- GitHub (that's Gizmo's domain)
- Slack admin functions
- Email sending (Jordan drafts, humans send)
- Financial systems or billing
- Any tool outside sales operations scope
