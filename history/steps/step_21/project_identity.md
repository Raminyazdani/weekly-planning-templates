# Project Identity: Weekly Calendar Planner

## Professional Identity

**Display Title:** Weekly Calendar Planner

**Repository Slug:** `weekly-calendar-planner`

**Tagline:** Automated weekly schedule visualization with recurring events and German holiday support

**GitHub Description:** 
A Python-based calendar planner that generates visual weekly schedules from CSV data with support for recurring events, multiple event types, and German holidays. Features a Flask API for programmatic entry submission.

**Primary Stack:**
- Python 3.x
- Flask (Web Framework)
- Pandas (Data Processing)
- Matplotlib (Visualization)
- workalendar (Holiday Handling)

**Topics/Keywords:**
- calendar-planner
- schedule-visualization
- python
- flask
- pandas
- matplotlib
- recurring-events
- weekly-planner
- time-management
- event-scheduling
- data-visualization

**Problem & Approach:**

**Problem Solved:**
Managing and visualizing weekly schedules with complex recurring patterns (daily, weekly, bi-weekly) across extended time periods is tedious with traditional calendar tools. Users need a flexible system that can generate calendar views from structured data and support programmatic event creation.

**Approach:**
This tool processes event data from CSV files with flexible recurrence rules (weekly, bi-weekly, daily, one-time events) and generates visual calendar representations. It creates a master calendar with German holidays, extends recurring events across date ranges, and produces high-quality PNG visualizations showing time-blocked schedules. A Flask API allows external systems to submit calendar entries programmatically.

**Inputs:**
- CSV files with event data (date ranges, times, recurrence patterns, event types, groups)
- Columns include: date start/end, type, group, day, recurrence flags (weekly/bi-weekly/one-time/daily), name, time start/end, status, location

**Outputs:**
- Main calendar visualization (PNG)
- Extended event data (CSV with resolved recurring events)
- Master calendar with holidays (CSV)
- Weekly frame visualizations (PNG files in frames/ directory)
- HTML table representation
- Flask API responses (JSON)
