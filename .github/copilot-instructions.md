# Copilot Instructions for RansomwareApp

## Project Overview
- **Purpose:** Interactive Gradio web app to educate users about ransomware warning signs, prevention tips, and visualize Google Trends data for security-related keywords.
- **Key Features:**
  - Tabbed UI: "Warning Signs", "Google Trends Explorer", "Prevention Tips"
  - Google Trends integration via `pytrends` (fetches and plots search interest)
  - Example keywords for quick exploration
  - All UI and logic in a single file: `ransomware.py`

## Architecture & Patterns
- **Single-file app:** All logic, UI, and data flow are in `ransomware.py`.
- **Class structure:**
  - `RansomwareApp`: Main app, manages UI and user interaction
  - `TrendsAPI`: Handles Google Trends data fetching and plotting
- **UI:** Built with Gradio's `Blocks` and `Tab` components. Markdown used for static content.
- **Data flow:**
  - User enters/selects a keyword → `analyze_keyword` → `TrendsAPI.fetch_google_trends` → returns plot and info

## Developer Workflows
- **Run locally:**
  - Install dependencies: `pip install gradio pytrends matplotlib pandas`
  - Start app: `python ransomware.py`
- **No build/test scripts:** No tests or build steps are present. App is run directly.
- **Plot output:** Trend chart is saved as `trend_plot.png` in the working directory (overwritten each time).

## Conventions & Notes
- **No persistent state:** App does not store user data or results between runs.
- **Error handling:** User-friendly error messages for failed Google Trends fetches.
- **FIXME/TODOs:**
  - Add chart description in the info tab (see `# FIXME` in code)
  - Consider chatbot tab (see code comment)
- **References:** CISA and No More Ransom Project are cited in the UI.

## Integration Points
- **External APIs:** Google Trends via `pytrends`
- **UI Framework:** Gradio
- **Plotting:** Matplotlib

## Example Usage
```bash
pip install gradio pytrends matplotlib pandas
python ransomware.py
```

---
For major changes, update this file to help future AI agents and developers quickly understand project structure and conventions.
