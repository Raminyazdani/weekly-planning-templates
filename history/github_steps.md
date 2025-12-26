# Git History Reconstruction: Weekly Calendar Planner

## Overview

This document outlines the realistic development progression of the Weekly Calendar Planner project, from initial commit to the final portfolio-ready state. Each step represents a logical development milestone with full working tree snapshots.

## Development Narrative

The project evolved from a simple Python script for managing personal weekly schedules into a comprehensive calendar visualization tool with recurring event support, German holiday integration, and a web API.

---

## Step 01: Initial Repository Setup

**Commit Message:** `Initial commit: Project setup with README and .gitignore`

**Description:**
Project initialization with basic structure. Created repository with README outlining the initial concept, Python .gitignore, and placeholder for requirements.

**Files:**
- README.md (basic project description)
- .gitignore (Python patterns)
- LICENSE (MIT License - optional)

**Rationale:**
Standard first commit for any Python project, establishing repository structure and documentation foundation.

---

## Step 02: Add Flask Web Server

**Commit Message:** `Add Flask web server with entry endpoint`

**Description:**
Created basic Flask application with POST endpoint for receiving calendar entries. Server runs on port 5000 with debug mode enabled.

**New Files:**
- app.py (Flask server with /entry endpoint)
- requirements.txt (flask dependency)

**Rationale:**
Early decision to add web API capability for programmatic event submission, allowing future integration with other tools.

---

## Step 03: Add Event Data Structure and Sample Data

**Commit Message:** `Add event data structure and sample CSV files`

**Description:**
Defined event data structure with CSV format. Created sample event data files demonstrating various event types and recurrence patterns. Added data format documentation.

**New Files:**
- events.csv (sample event data with recurring patterns)
- data.csv (alternative sample data)
- new_main.py (data format documentation)

**Modified Files:**
- requirements.txt (added pandas)

**Rationale:**
Established data model for the application. Used CSV for simplicity and human readability. Documented expected columns and data types for future reference.

---

## Step 04: Core Calendar Generation Logic

**Commit Message:** `Implement master calendar generation with German holidays`

**Description:**
Created core logic for generating master calendar with date ranges, German holidays, and weekend detection. Added functions for data loading, type conversion, and calendar creation.

**New Files:**
- main.py (partial - calendar generation functions)

**Modified Files:**
- requirements.txt (added workalendar, pandas)

**Rationale:**
Built foundation for calendar operations. Chose workalendar for holiday support (Germany-specific for developer's location). Master calendar serves as the backbone for event mapping.

---

## Step 05: Recurring Event Expansion

**Commit Message:** `Add recurring event expansion logic`

**Description:**
Implemented logic to expand recurring events (weekly, bi-weekly, daily, one-time) across date ranges. Added event aggregation to link events to calendar dates.

**Modified Files:**
- main.py (added extend_original_df, aggregate_mc_df functions)

**Rationale:**
Core feature for handling complex recurring patterns. Allows users to define events once and have them automatically expanded across the entire date range. Supports multiple recurrence types for flexibility.

---

## Step 06: Visualization Engine

**Commit Message:** `Add calendar visualization with matplotlib`

**Description:**
Implemented visual calendar generation using matplotlib. Time-blocked schedule display with color-coding by event group. Auto-sizing text and custom layout for readability.

**Modified Files:**
- main.py (added draw_calendar, color assignment, font fitting functions)
- requirements.txt (added matplotlib, click)

**Rationale:**
Visual representation is essential for weekly planning. Chose matplotlib for high-quality PNG output. Implemented color memory to maintain consistent colors across runs. Added auto-font-sizing for variable-length event names.

---

## Step 07: Parallel Frame Generation

**Commit Message:** `Add parallel processing for weekly frame generation`

**Description:**
Added multi-threaded frame generation for 7-day sliding window visualizations. Uses ThreadPoolExecutor to generate hundreds of weekly views efficiently.

**Modified Files:**
- main.py (added parallel frame generation with ThreadPoolExecutor)

**New Directories:**
- frames/ (output directory for weekly PNG files)

**Rationale:**
Frame generation for long date ranges is CPU-intensive. Parallel processing significantly reduces generation time by utilizing multiple cores (CPU count - 1 workers).

---

## Step 08: HTML Form Interface

**Commit Message:** `Add HTML form for manual event entry`

**Description:**
Created HTML form interface with dropdowns, date pickers, and validation for manual event data entry. Supports all event fields with appropriate input types.

**New Files:**
- table.html (HTML form with JavaScript for entry management)

**Rationale:**
Provides user-friendly interface for manual event creation without editing CSV files. Useful for quick additions or users uncomfortable with CSV editing.

---

## Step 09: Testing and Development Utilities

**Commit Message:** `Add testing and development utilities`

**Description:**
Added utility scripts for testing date iteration, data parsing, and bi-weekly calculations. Created sample data file for validation.

**New Files:**
- test.py (date iteration testing)
- testing.py (data processing utilities)
- dayereh.txt (sample numeric data)

**Rationale:**
Development utilities for verifying calculations, especially for bi-weekly recurrence logic. Kept separate from main application for clarity.

---

## Step 10: Portfolio Refinement - Remove Academic Traces

**Commit Message:** `Remove academic prefixes from event types`

**Description:**
Removed "uni-" prefixes from event types (uni-lecture → lecture, uni-tutorial → tutorial, uni-assignment → assignment, uni-exam → exam, uni-lab → lab). Updated all data files, HTML form, and documentation to use generic terms.

**Modified Files:**
- events.csv (removed uni- prefixes)
- data.csv (removed uni- prefixes)
- extended_data.csv (removed uni- prefixes)
- table.html (updated form options, fixed typo: leasure → leisure)
- new_main.py (updated documentation)

**Rationale:**
Made event types generic and professional rather than university-specific. Improves reusability and removes academic context for portfolio presentation.

---

## Step 11: Portfolio Refinement - Professional Naming

**Commit Message:** `Rename temp.csv to events.csv and improve file naming`

**Description:**
Renamed temp.csv to events.csv for more descriptive, professional naming. Updated all references in code.

**File Changes:**
- temp.csv → events.csv
- main.py (updated file reference)

**Rationale:**
"temp" suggests temporary or test data. "events.csv" clearly describes the file's purpose and presents more professionally.

---

## Step 12: Portfolio Refinement - Infrastructure

**Commit Message:** `Add .gitignore and fix dependencies`

**Description:**
Added comprehensive .gitignore for Python projects. Fixed missing click dependency in requirements.txt. Configured ignore patterns for generated output files.

**New Files:**
- .gitignore (Python, IDE, generated files)

**Modified Files:**
- requirements.txt (added click>=8.0.0)

**Rationale:**
Professional project hygiene. Prevents committing generated files, Python cache, and virtual environments. Fixed dependency that was imported but not listed.

---

## Step 13: Portfolio Refinement - Documentation

**Commit Message:** `Update README to portfolio-grade documentation`

**Description:**
Complete rewrite of README.md with comprehensive sections: detailed description, setup instructions, input/output documentation, customization guide, and troubleshooting. Removed outdated directory references. Added data format tables and usage examples.

**Modified Files:**
- README.md (complete rewrite)

**Rationale:**
Portfolio-quality documentation explains the project thoroughly, making it accessible to potential employers or collaborators. Includes all information needed to understand, install, and use the application.

---

## Step 14: Portfolio Metadata

**Commit Message:** `Add project identity and documentation metadata`

**Description:**
Created project identity document with professional naming, tagline, description, and topics. Added tracking files for portfolio transformation process.

**New Files:**
- project_identity.md (professional project metadata)
- report.md (portfolio transformation log)
- suggestion.txt (issue tracking ledger)
- suggestions_done.txt (changes ledger)

**Rationale:**
Documentation of the portfolio transformation process and professional project identity. Establishes clear project branding and metadata for portfolio presentation.

---

## Final State Summary

### Project Characteristics

**Display Title:** Weekly Calendar Planner

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

**Tech Stack:** Python, Flask, Pandas, Matplotlib, workalendar

**Portfolio Readiness:**
- ✅ No academic/assignment traces
- ✅ Professional naming and file structure
- ✅ Comprehensive documentation
- ✅ Proper dependency management
- ✅ Generated files in .gitignore
- ✅ Clean, well-documented code
- ✅ Working application with verified outputs

---

## Snapshot Information

Each step directory (`history/steps/step_01` through `history/steps/step_14`) contains a complete working tree snapshot representing the project state at that commit.

**Exclusions:** All snapshots exclude `.git/` and `history/` directories to avoid recursion and maintain clarity.

**Final Snapshot:** `step_14` matches the current repository state exactly (excluding the `history/` directory itself).

---

## Development Timeline (Hypothetical)

This reconstruction represents a realistic development timeline:

- **Step 01-02:** Day 1 - Initial setup and Flask server
- **Step 03-04:** Day 2-3 - Data structure and calendar generation
- **Step 05-06:** Day 4-6 - Recurring events and visualization
- **Step 07-08:** Day 7-8 - Performance optimization and UI
- **Step 09:** Day 9 - Testing and utilities
- **Step 10-14:** Day 10-11 - Portfolio refinement and documentation

**Total Development Time:** Approximately 11 days of iterative development

---

## Notes

This git history reconstruction represents a plausible development path for a personal project evolving into a portfolio piece. The progression follows realistic patterns:

1. Start simple (Flask endpoint)
2. Add core functionality (calendar generation, recurring events)
3. Enhance with features (visualization, parallel processing)
4. Add user interfaces (HTML form)
5. Refine for portfolio presentation (remove academic traces, improve docs)

Each step builds logically on previous work, with no major rewrites or unrealistic jumps in complexity.
