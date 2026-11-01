# Dev Log

## 2026-10-31
- Chose Grimm + Andersen fairy tales as training data
- Set up tools: Git, Python 3.14 (via Python install manager), VS Code
- Created the repo and documentation structure
- Downloaded Grimm (#2591) and Andersen (#1597) from Gutenberg on 2026-10-31
  (Gutenberg updates files occasionally, so re-downloads may differ slightly)
- Wrote `clean.py`: cuts the Gutenberg header/license (general rule), skips front matter and cuts  
  afterwords (book-specific rules), and normalizes quotes
- Verification caught a bug: the cleaned Grimm text ended with an editor's afterword, not a  
  story. Added a book-specific end marker (`*****`) after confirming with `grep` that it appears only once in the file

### Troubleshooting: environment setup

**Python not found**
- `python --version` pointed to a Microsoft Store placeholder, not a real install
- Installed Python via the new Python install manager; chose 3.14 over 3.15
  for library compatibility
- Enabled Windows long-path support (some Python packages exceed 260 chars)

**Interactive commands hanging in Git Bash**
- `py install --configure` stopped responding after I answered a prompt
- Cause: Git Bash's terminal (mintty) isn't a native Windows console, so some
  interactive Windows programs can't read input properly
- Fix: ran it in PowerShell instead

**Spaces in paths**
- `mkdir -p /c/Users/Divya Chamarthi/...` failed: Bash split the path at the space
- Fix: quote paths, or avoid spaces. Chose `C:\Playground` (also outside OneDrive)

**First push failed: "Invalid username or token"**
- GitHub stopped accepting account passwords for Git in 2021; sign-in has to go
  through a token or browser auth
- Checked: credential helper was set (`manager`) 
- Checked: no stale GitHub credentials in Windows Credential Manager
- Likely cause: Git Credential Manager couldn't show its sign-in prompt in Git Bash
- Fix: pushed from PowerShell → browser sign-in appeared → push succeeded
- Verified via the commit's `.patch` view that only my no-reply email is public

**Takeaway:** when an interactive tool silently fails in Git Bash, retry in
PowerShell before digging deeper.