# Portfolio Readiness Report: Weekly Planning Templates

## Execution Log

### PHASE 0 - Initial Self-Setup

**Date:** 2025-12-26

**0.1 Create Required Files:**
- Created `report.md` (this file)
- Will create `suggestion.txt`, `suggestions_done.txt`, `project_identity.md` next

**0.2 Copilot Guidance:**
- Existing `.github/copilot-instructions.md` found and reviewed
- Instructions are appropriate for this single-project repository

---

## Repository Initial State

### Files Found:
- Python files: `main.py`, `app.py`, `new_main.py`, `test.py`, `testing.py`
- Data files: `data.csv`, `temp.csv`, `extended_data.csv`, `master_calendar.csv`
- Output files: `calendar.png`, `table.html`, `dayereh.txt`
- Directory: `frames/` (contains ~100+ generated calendar PNG files)
- Documentation: `README.md`, `requirements.txt`

### Initial Assessment:
- **No obvious academic/assignment traces** in file names or README
- **No absolute paths** detected in main code files
- Code structure is flat but functional
- Multiple file versions suggest iterative development
- Project appears to be a personal calendar planner with German holiday support
- Flask web server with POST endpoint for entries
- Main logic generates weekly calendar visualizations from CSV data

---

## PHASE 1 - Understanding & Target Identity

### Project Understanding

**Domain/Problem:**
Weekly calendar planning and visualization with support for recurring events across extended time periods (e.g., semester schedules).

**Method/Approach:**
- CSV-based event data input with flexible recurrence patterns
- Master calendar generation with German holiday integration
- Visual rendering using Matplotlib with time-blocking
- Flask API for programmatic event submission
- Parallel processing for generating weekly frame visualizations

**Expected Inputs:**
- CSV files with columns: date start/end, type, group, day, recurrence flags, name, time start/end, status, location
- Recurrence patterns: daily, weekly, bi-weekly, one-time

**Produced Outputs:**
- Main calendar visualization (calendar.png)
- Extended event data (extended_data.csv) - resolved recurring events
- Master calendar (master_calendar.csv) - date range with holidays
- Weekly frames (frames/*.png) - 7-day sliding window visualizations
- HTML form (table.html) - data entry interface

**Primary Stack:**
Python, Flask, Pandas, Matplotlib, workalendar

**Current Structure:**
- Flat structure (all files in root)
- Multiple file versions (main.py, new_main.py, test.py, testing.py)
- No .gitignore

### Professional Identity Decision

**Display Title:** Weekly Calendar Planner
**Repo Slug:** weekly-calendar-planner
**Tagline:** Automated weekly schedule visualization with recurring events and German holiday support

(Full details in project_identity.md)

### Naming Alignment Plan

**Issues Identified:**

1. **Academic Traces in Data (CRITICAL):**
   - Event types contain "uni-" prefix: uni-lecture, uni-tutorial, uni-assignment, uni-exam, uni-lab
   - Found in: temp.csv, data.csv, extended_data.csv, table.html, new_main.py
   - **Action:** Replace with generic types: lecture, tutorial, assignment, exam, lab

2. **File Naming Issues:**
   - temp.csv → should be events.csv or schedule.csv (more descriptive)
   - main.py references 'temp.csv' at line 472

3. **Development Artifacts:**
   - test.py, testing.py, new_main.py appear to be development/iteration files
   - **Action:** Assess and either consolidate, document purpose, or archive

4. **Documentation Issues:**
   - README references obsolete directory name "weekly planner"
   - new_main.py purpose unclear

5. **Missing Infrastructure:**
   - No .gitignore file
   - Generated files committed: frames/, extended_data.csv, master_calendar.csv, calendar.png

6. **Unclear Files:**
   - dayereh.txt - contains numbers, used by testing.py, unclear business purpose

7. **Dependency Issue:**
   - main.py imports 'click' but requirements.txt doesn't include it

**Alignment Approach:**
Conservative, safety-first approach:
- Remove "uni-" prefixes from all event types
- Rename temp.csv → events.csv
- Create .gitignore for generated files
- Clean up development artifacts
- Add missing dependency
- Update documentation
- NO major structural refactoring (keep flat structure as it's simple and functional)

---

## PHASE 2 - Pre-Change Audit

**Date:** 2025-12-26

### Audit Results

Systematic scan completed. All findings documented in suggestion.txt with:
- 15 issues identified
- Categories: TRACE (5), RENAME (2), STRUCTURE (4), DOC (2), OTHER (2)
- No absolute paths found (✓)
- No obvious security issues (✓)

### Key Findings Summary:

**Academic Traces:** University-specific event type prefixes in data and forms
**Naming Issues:** Temporary file names, unclear purpose files
**Infrastructure Gaps:** Missing .gitignore, generated files in git
**Documentation:** Outdated directory references, unclear file purposes
**Dependencies:** Missing 'click' in requirements.txt

All findings logged in suggestion.txt with TAB-separated format as required.

---

## PHASE 3 - Portfolio-Readiness Changes

(To be continued as changes are applied...)
