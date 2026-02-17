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

### Granola
- **Purpose:** Access meeting notes, transcripts, and action items from sales calls
- **MCP URL:** `https://mcp.granola.ai/mcp`
- **Auth:** OAuth (browser-based sign-in flow — no API key required)
- **Permissions:** Read-only access to meeting notes owned by the authenticated user
- **Rules:**
  - Use meeting notes to keep deal records accurate after sales calls
  - Cross-reference meeting notes with HubSpot deal data when updating records
  - Only notes where the authenticated user is the owner are accessible
  - Do not store or reproduce full transcripts outside of structured deal updates

### gogcli (Google Workspace)
- **Purpose:** Read and write Google Drive files, Docs, and Sheets — proposals, briefs, pipeline spreadsheets, templates
- **Integration:** CLI tool (`gog`) — not MCP. Invoked via Bash.
- **Auth:** OAuth2 desktop flow. Tokens stored in macOS Keychain. Account: `y@vezadigital.com`
- **Permissions:** Drive (read/write), Docs (read/write), Sheets (read/write), Drive Meet (read-only)
- **Key commands:**
  - `gog drive ls --query "name contains 'keyword'" --account y@vezadigital.com` — search files
  - `gog docs get <docId> --account y@vezadigital.com` — read a Google Doc
  - `gog sheets get <spreadsheetId> <range> --account y@vezadigital.com` — read sheet data
  - `gog sheets metadata <spreadsheetId> --account y@vezadigital.com` — get sheet structure
- **Rules:**
  - Always pass `--account y@vezadigital.com` (or set `GOG_ACCOUNT` env var)
  - For write operations on Docs/Sheets, confirm with the team first (same rule as HubSpot)
  - Do not download or cache large files locally — read content in-memory via CLI output
  - If a file returns a 403, flag it as a permissions issue rather than retrying

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
