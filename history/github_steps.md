# Git History Reconstruction: Weekly Calendar Planner (Step-Expanded Edition)

## History Expansion Note

**Previous Run:** N_old = 14 steps  
**Current Run:** N_new = 21 steps  
**Expansion Multiplier:** 21/14 = **1.5×** (exactly meeting the minimum requirement)

### Old Step Groups → New Step Ranges Mapping

| Old Step(s) | New Step(s) | Expansion Type | Description |
|-------------|-------------|----------------|-------------|
| Step 01 | Step 01 | Direct | Initial setup (unchanged) |
| Step 02 | Step 02 | Direct | Flask server (unchanged) |
| Step 03 | Steps 03-04 | **Oops→Hotfix** | Event data + API endpoint typo fix |
| Step 04 | Steps 05-06 | Split | Calendar logic divided: date range + holidays |
| Step 05 | Step 07 | Direct | Recurring events (unchanged) |
| Step 06 | Steps 08-10 | Split | Visualization divided: plotting + colors + fonts |
| Step 07 | Steps 11-12 | Split | Frame generation: single-thread + parallel |
| Step 08 | Steps 13-14 | **Oops→Hotfix** | HTML form + typo fix |
| Step 09 | Step 15 | Direct | Testing utilities (unchanged) |
| Step 10 | Step 16 | Direct | Remove academic prefixes (unchanged) |
| Step 11 | Step 17 | Direct | Rename temp.csv (unchanged) |
| Step 12 | Step 18 | Direct | Infrastructure (.gitignore) (unchanged) |
| Step 13 | Steps 19-20 | Split | README divided: structure + detailed content |
| Step 14 | Step 21 | Direct | Portfolio metadata (FINAL) |

### Oops → Hotfix Sequences Inserted

#### Sequence #1: Flask Endpoint Typo (Steps 03→04)

**What broke:** In step 03, the Flask endpoint was incorrectly defined as `@app.post("/entrey")` instead of `@app.post("/entry")` due to a typo.

**How noticed:** When testing the API endpoint after implementation, POST requests to `/entry` returned 404 errors. Quick code review revealed the typo in the decorator.

**How fixed:** Step 04 corrected the endpoint path from `/entrey` to `/entry` in app.py, immediately resolving the routing issue.

**Files affected:** `app.py` (line 5)

**Impact:** This is a realistic mistake - typos in route definitions are common and immediately noticeable when testing endpoints manually or with tools like curl/Postman.

#### Sequence #2: HTML Form Typo (Steps 13→14)

**What broke:** In step 13, the HTML form had an event type option spelled as "leasure" instead of "leisure" throughout the file.

**How noticed:** While manually testing the form interface, the misspelling was visible in the dropdown options. This would affect data consistency if users selected this option.

**How fixed:** Step 14 corrected all instances of "leasure" to "leisure" in table.html, ensuring proper spelling in the UI.

**Files affected:** `table.html` (option values and labels)

**Impact:** This represents a realistic typo that could slip through initial development but would be caught during UI testing or by the first user to interact with the form.

---

## Overview

This document outlines the realistic development progression of the Weekly Calendar Planner project, from initial commit to the final portfolio-ready state. Each step represents a logical development milestone with full working tree snapshots.

The project evolved from a simple Python script for managing personal weekly schedules into a comprehensive calendar visualization tool with recurring event support, German holiday integration, and a web API.

---

## Step 01: Initial Repository Setup

**Commit Message:** `Initial commit: Project setup with README and .gitignore`

**Description:**
Project initialization with basic structure. Created repository with README outlining the initial concept, Python .gitignore, and placeholder for requirements.

**Files Added:**
- README.md (basic project description)
- .gitignore (Python patterns)
- requirements.txt (empty placeholder)

**Rationale:**
Standard first commit for any Python project, establishing repository structure and documentation foundation.

---

## Step 02: Add Flask Web Server

**Commit Message:** `Add Flask web server with entry endpoint`

**Description:**
Created basic Flask application with POST endpoint for receiving calendar entries. Server runs on port 5000 with debug mode enabled.

**Files Added:**
- app.py (Flask server with /entry endpoint)

**Files Modified:**
- requirements.txt (added flask)

**Rationale:**
Early decision to add web API capability for programmatic event submission, allowing future integration with other tools.

---

## Step 03: Add Event Data Structure [OOPS: Contains Typo]

**Commit Message:** `Add event data structure and sample CSV files`

**Description:**
Defined event data structure with CSV format. Created sample event data files demonstrating various event types and recurrence patterns. Added data format documentation.

**⚠️ BUG INTRODUCED:** Flask endpoint has typo: `/entrey` instead of `/entry`

**Files Added:**
- data.csv (sample event data)
- new_main.py (data format documentation)

**Files Modified:**
- requirements.txt (added pandas)
- app.py (contains typo in route decorator)

**Rationale:**
Established data model for the application. Used CSV for simplicity and human readability. Documented expected columns and data types for future reference.

---

## Step 04: Fix Flask Endpoint Typo [HOTFIX]

**Commit Message:** `Fix typo in Flask endpoint path`

**Description:**
Corrected Flask route decorator from `/entrey` to `/entry`. Bug was discovered during manual API testing when POST requests returned 404 errors.

**Files Modified:**
- app.py (fixed route path: `/entrey` → `/entry`)

**Rationale:**
Quick hotfix to resolve routing issue. This type of typo is common during rapid development and typically caught during first manual test of the endpoint.

---

## Step 05: Core Calendar Generation - Date Ranges

**Commit Message:** `Implement master calendar date range generation`

**Description:**
Created core logic for generating master calendar with date ranges and weekend detection. Added functions for data loading, type conversion, and basic calendar creation.

**Files Added:**
- main.py (calendar generation functions)

**Files Modified:**
- requirements.txt (added pandas)

**Rationale:**
Built foundation for calendar operations. Master calendar with date range serves as the backbone for event mapping. Weekend detection helps identify non-working days.

---

## Step 06: Core Calendar Generation - German Holidays

**Commit Message:** `Add German holiday integration to master calendar`

**Description:**
Enhanced master calendar with German holiday support using workalendar library. Added holiday labels and IsOffDay flag combining holidays and weekends.

**Files Modified:**
- main.py (added Germany calendar, holiday detection, IsOffDay logic)
- requirements.txt (added workalendar)

**Rationale:**
Holiday integration essential for realistic schedule planning. Chose workalendar for comprehensive German holiday support (developer's location). Combined holidays and weekends into unified IsOffDay indicator.

---

## Step 07: Recurring Event Expansion

**Commit Message:** `Add recurring event expansion logic`

**Description:**
Implemented logic to expand recurring events (weekly, bi-weekly, daily, one-time) across date ranges. Added event aggregation to link events to calendar dates.

**Files Modified:**
- main.py (added extend_original_df, aggregate_mc_df functions)

**Rationale:**
Core feature for handling complex recurring patterns. Allows users to define events once and have them automatically expanded across the entire date range. Supports multiple recurrence types for flexibility.

---

## Step 08: Visualization Engine - Basic Plotting

**Commit Message:** `Add basic calendar visualization with matplotlib`

**Description:**
Implemented initial visual calendar generation using matplotlib. Basic time-blocked schedule display with matplotlib figure and axis setup.

**Files Modified:**
- main.py (added draw_calendar function with basic plotting)
- requirements.txt (added matplotlib, click)

**Rationale:**
Visual representation is essential for weekly planning. Chose matplotlib for high-quality PNG output. Started with basic plotting structure to establish rendering pipeline.

---

## Step 09: Visualization Engine - Color Coding

**Commit Message:** `Add color coding by event group with persistent colors`

**Description:**
Enhanced visualization with color-coding by event group. Implemented color memory system to maintain consistent colors for groups across runs using color dictionary persistence.

**Files Modified:**
- main.py (added color assignment, color dictionary management)

**Rationale:**
Color-coding improves readability by visually distinguishing event groups. Color persistence ensures consistent user experience across multiple executions. Uses hash-based color generation for automatic assignment.

---

## Step 10: Visualization Engine - Auto Font Sizing

**Commit Message:** `Add automatic font sizing for event text`

**Description:**
Implemented auto-sizing text fitting for event names. Event text automatically scales down to fit within time blocks, handling variable-length event names gracefully.

**Files Modified:**
- main.py (added font fitting functions, auto-resize logic)

**Rationale:**
Event names vary in length. Auto-sizing ensures all text is readable regardless of length while maximizing font size for better visibility. Prevents text overflow in calendar cells.

---

## Step 11: Frame Generation - Sequential Implementation

**Commit Message:** `Add 7-day sliding window frame generation`

**Description:**
Added weekly frame generation for creating multiple 7-day sliding window visualizations. Initial implementation processes frames sequentially.

**Files Modified:**
- main.py (added frame generation logic, sequential processing)

**Directories Created:**
- frames/ (output directory for weekly PNG files)

**Rationale:**
Frame generation allows users to browse through extended schedules week by week. Started with sequential processing to verify correctness before optimization.

---

## Step 12: Frame Generation - Parallel Optimization

**Commit Message:** `Optimize frame generation with parallel processing`

**Description:**
Converted frame generation to multi-threaded parallel processing using ThreadPoolExecutor. Utilizes CPU count - 1 workers for efficient multi-core utilization.

**Files Modified:**
- main.py (replaced sequential with parallel frame generation using ThreadPoolExecutor)

**Rationale:**
Frame generation for long date ranges is CPU-intensive (can generate 100+ frames). Parallel processing significantly reduces generation time by utilizing multiple cores while leaving one core for system tasks.

---

## Step 13: HTML Form Interface [OOPS: Contains Typo]

**Commit Message:** `Add HTML form for manual event entry`

**Description:**
Created HTML form interface with dropdowns, date pickers, and validation for manual event data entry. Supports all event fields with appropriate input types.

**⚠️ BUG INTRODUCED:** Event type dropdown contains "leasure" instead of "leisure"

**Files Added:**
- table.html (HTML form with JavaScript, contains spelling error)

**Rationale:**
Provides user-friendly interface for manual event creation without editing CSV files. Useful for quick additions or users uncomfortable with CSV editing.

---

## Step 14: Fix HTML Form Spelling Error [HOTFIX]

**Commit Message:** `Fix spelling: leasure → leisure in HTML form`

**Description:**
Corrected spelling error in HTML form event type options. Changed "leasure" to "leisure" throughout the form to ensure proper spelling consistency.

**Files Modified:**
- table.html (corrected spelling in option values and labels)

**Rationale:**
Spelling errors in UI are unprofessional and can affect data consistency. This fix ensures the form presents properly spelled options to users and maintains data quality.

---

## Step 15: Testing and Development Utilities

**Commit Message:** `Add testing and development utilities`

**Description:**
Added utility scripts for testing date iteration, data parsing, and bi-weekly calculations. Created sample data file for validation.

**Files Added:**
- test.py (date iteration testing)
- testing.py (data processing utilities)
- dayereh.txt (sample numeric data)

**Rationale:**
Development utilities for verifying calculations, especially for bi-weekly recurrence logic. Kept separate from main application for clarity. Useful for debugging and validation during development.

---

## Step 16: Portfolio Refinement - Remove Academic Traces

**Commit Message:** `Remove academic prefixes from event types`

**Description:**
Removed "uni-" prefixes from event types (uni-lecture → lecture, uni-tutorial → tutorial, uni-assignment → assignment, uni-exam → exam, uni-lab → lab). Updated all data files, HTML form, and documentation to use generic terms.

**Files Modified:**
- events.csv (removed uni- prefixes)
- data.csv (removed uni- prefixes)
- extended_data.csv (removed uni- prefixes)
- table.html (updated form options, fixed any remaining typos)
- new_main.py (updated documentation)

**Rationale:**
Made event types generic and professional rather than university-specific. Improves reusability and removes academic context for portfolio presentation. Makes the tool applicable to any scheduling context.

---

## Step 17: Portfolio Refinement - Professional Naming

**Commit Message:** `Rename temp.csv to events.csv`

**Description:**
Renamed temp.csv to events.csv for more descriptive, professional naming. Updated all references in code.

**File Changes:**
- temp.csv → events.csv (renamed)
- main.py (updated file reference at line 472)

**Rationale:**
"temp" suggests temporary or test data. "events.csv" clearly describes the file's purpose and presents more professionally. Important for portfolio presentation.

---

## Step 18: Portfolio Refinement - Infrastructure

**Commit Message:** `Add .gitignore and fix dependencies`

**Description:**
Added comprehensive .gitignore for Python projects. Fixed missing click dependency in requirements.txt. Configured ignore patterns for generated output files.

**Files Added:**
- .gitignore (Python, IDE, generated files)

**Files Modified:**
- requirements.txt (added click>=8.0.0)

**Rationale:**
Professional project hygiene. Prevents committing generated files, Python cache, and virtual environments. Fixed dependency that was imported but not listed. Essential for portfolio quality.

---

## Step 19: Portfolio Refinement - README Structure

**Commit Message:** `Add comprehensive README structure and sections`

**Description:**
Major README expansion adding structure for portfolio-grade documentation. Added sections for description, tech stack, repository structure, setup instructions, and usage examples.

**Files Modified:**
- README.md (added structure, table of contents, basic section headers)

**Rationale:**
First phase of README improvement focused on establishing comprehensive documentation structure. Sets up sections that will be filled with detailed content in next step.

---

## Step 20: Portfolio Refinement - README Detailed Content

**Commit Message:** `Add detailed README content and examples`

**Description:**
Complete README content fill-out with detailed descriptions, input/output documentation, customization guide, and troubleshooting. Removed outdated directory references. Added data format tables and comprehensive usage examples.

**Files Modified:**
- README.md (filled in all sections with detailed content, examples, tables)

**Rationale:**
Portfolio-quality documentation explains the project thoroughly, making it accessible to potential employers or collaborators. Includes all information needed to understand, install, and use the application. Clear troubleshooting helps users resolve common issues.

---

## Step 21: Portfolio Metadata and Final State

**Commit Message:** `Add project identity and portfolio documentation`

**Description:**
Created project identity document with professional naming, tagline, description, and topics. Added tracking files for portfolio transformation process. Final portfolio-ready state with all metadata and documentation complete.

**Files Added:**
- project_identity.md (professional project metadata)
- report.md (portfolio transformation log)
- suggestion.txt (issue tracking ledger)
- suggestions_done.txt (changes ledger)

**Files Modified:**
- .github/ (updated with current infrastructure)

**Rationale:**
Documentation of the portfolio transformation process and professional project identity. Establishes clear project branding and metadata for portfolio presentation. Final step brings project to production-ready portfolio quality.

---

## Final State Summary

### Project Characteristics

**Display Title:** Weekly Calendar Planner

**Repository:** weekly-calendar-planner

**Description:** A Python-based calendar planner that generates visual weekly schedules from CSV data with support for recurring events, multiple event types, and German holidays. Features a Flask API for programmatic entry submission.

**Key Features:**
- Recurring event expansion (daily, weekly, bi-weekly, one-time)
- German holiday integration
- Visual time-blocked calendar generation
- Color-coded event groups with persistent colors
- Parallel weekly frame generation
- Flask API for programmatic entry
- HTML form for manual entry
- Comprehensive CSV data format

**Tech Stack:** Python, Flask, Pandas, Matplotlib, workalendar, ThreadPoolExecutor

**Portfolio Readiness:**
- ✅ No academic/assignment traces
- ✅ Professional naming and file structure
- ✅ Comprehensive documentation
- ✅ Proper dependency management
- ✅ Generated files in .gitignore
- ✅ Clean, well-documented code
- ✅ Working application with verified outputs
- ✅ Realistic git history with incremental development

---

## Snapshot Information

Each step directory (`history/steps/step_01` through `history/steps/step_21`) contains a complete working tree snapshot representing the project state at that commit.

**Exclusions:** All snapshots exclude `.git/` and `history/` directories to avoid recursion and maintain clarity.

**Final Snapshot:** `step_21` matches the current repository state exactly (excluding the `history/` directory itself).

---

## Development Timeline (Hypothetical)

This reconstruction represents a realistic development timeline spanning approximately 14 days:

- **Day 1:** Steps 01-02 - Initial setup, Flask server
- **Day 2:** Steps 03-04 - Event data structure + API typo fix
- **Day 3-4:** Steps 05-06 - Calendar generation (date ranges + holidays)
- **Day 5:** Step 07 - Recurring event expansion
- **Day 6-7:** Steps 08-10 - Visualization (plotting + colors + fonts)
- **Day 8-9:** Steps 11-12 - Frame generation (sequential + parallel)
- **Day 10:** Steps 13-14 - HTML form + typo fix
- **Day 11:** Step 15 - Testing utilities
- **Day 12:** Steps 16-17 - Remove academic traces, professional naming
- **Day 13:** Steps 18-20 - Infrastructure, README documentation
- **Day 14:** Step 21 - Portfolio metadata and final polish

**Total Development Time:** Approximately 14 days of iterative development with realistic mistakes and fixes.

---

## Notes on Step Expansion

This step-expanded history (21 steps vs. original 14) demonstrates realistic development patterns:

1. **Incremental Feature Building:** Large features (calendar, visualization, frames) broken into smaller, testable commits
2. **Real Mistakes:** Two oops→hotfix sequences show authentic development including typos and quick corrections
3. **Performance Optimization:** Separate commits for initial implementation vs. optimization (e.g., sequential → parallel)
4. **Documentation Evolution:** README development split into structure vs. content phases
5. **Quality Progression:** Portfolio refinement spread across multiple focused commits

Each step builds logically on previous work, with no major rewrites or unrealistic jumps in complexity. The expansion maintains narrative coherence while increasing granularity to show more realistic development progression.

The 1.5× expansion multiplier was achieved through:
- **4 split commits** (steps 4, 6, 7, 13 → became 7 steps)
- **2 oops→hotfix sequences** (added 2 steps)
- **7 direct carries** (unchanged steps)

Total: 14 original → 21 expanded (exactly 1.5× multiplier)
