---
name: fetch-doc
description: Fetches content from Google Drive, Docs, or Sheets using gogcli.
  Trigger phrases include "pull the doc", "grab the brief", "get the spreadsheet",
  "find the proposal", "what's in the [doc name]".
---

# Fetch Doc

## Purpose

Pull content from Google Workspace files — Docs, Sheets, or any Drive file — so Jordan can reference it in deal workflows. Common use cases: reading proposal drafts, pulling internal briefs, checking pipeline spreadsheets, or grabbing templates.

## Prerequisites

- `gogcli` installed and authorized (`gog auth ls` should show an active account)
- `GOG_ACCOUNT` environment variable set, or pass `--account` per command

## Inputs

**Required:**
- A file identifier: file name (for search), Google Drive file ID, or a Google Docs/Sheets URL

**Optional:**
- Specific sheet name or cell range (for Sheets)
- Output format preference (summary vs. full content)

## Workflow

1. **Identify the file.**
   - If given a name or keyword, search Drive:
     ```bash
     gog drive ls --query "name contains '[keyword]'" --account y@vezadigital.com
     ```
   - If given a URL, extract the file ID from it (the long string between `/d/` and `/edit` or `/view`)
   - If given a file ID directly, use it as-is

2. **Determine file type and fetch content.**

   **Google Doc:**
   ```bash
   gog docs get <docId> --account y@vezadigital.com
   ```

   **Google Sheet:**
   ```bash
   # Full sheet
   gog sheets get <spreadsheetId> <range> --account y@vezadigital.com

   # Specific range
   gog sheets get <spreadsheetId> "Sheet1!A1:D20" --account y@vezadigital.com

   # Sheet metadata (tab names, row counts)
   gog sheets metadata <spreadsheetId> --account y@vezadigital.com
   ```

   **Other file (PDF, image, etc.):**
   ```bash
   gog drive download <fileId> --account y@vezadigital.com
   ```

3. **Present the content.** Format based on context:
   - If the user needs a quick reference, summarize the key points
   - If the user needs the full content (e.g., for a deal update), present it structured
   - For spreadsheets, render as a clean table

4. **Flag issues.** If the file can't be found, access is denied, or content looks stale, say so.

## Output Format

```
## 📄 [File Name]
**Type:** Google Doc | Google Sheet | PDF | Other
**Last modified:** [date]
**Link:** [Google Drive URL]

### Content
[File content or summary, formatted appropriately]
```

For spreadsheets:

```
## 📊 [Spreadsheet Name]
**Sheet:** [tab name]
**Range:** [cell range if specified]

| Col A | Col B | Col C |
|-------|-------|-------|
| ...   | ...   | ...   |
```

## Common Patterns

**"Pull the Garner Health brief"**
→ Search Drive for "Garner Health" → find the Doc → fetch and display content

**"What's in the pipeline spreadsheet?"**
→ Search Drive for "pipeline" → fetch sheet metadata → read relevant range

**"Grab the proposal template"**
→ Search Drive for "proposal template" → fetch the Doc → present for reference

## Edge Cases

- **Multiple matches:** If a name search returns several files, list them and ask which one.
- **Large spreadsheets:** Fetch metadata first to understand the structure, then read specific ranges rather than dumping the entire sheet.
- **Permission errors:** If `gog` returns a 403, tell the user: "I can't access that file — check sharing permissions for y@vezadigital.com."
- **Stale content:** If `last modified` is more than 30 days old, flag it: "Heads up — this file hasn't been updated since [date]."
