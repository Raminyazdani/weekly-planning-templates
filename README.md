# Weekly Calendar Planner

**Tagline:** Automated weekly schedule visualization with recurring events and German holiday support

**Project Type:** Personal Project  
**Primary Stack:** Python/Flask

## Description

A Python-based calendar planner that generates visual weekly schedules from CSV data with support for recurring events, multiple event types, and German holidays. Features a Flask API for programmatic entry submission and parallel processing for generating calendar visualizations.

## What It Does

This calendar planner solves the challenge of managing and visualizing complex recurring schedules across extended time periods. Instead of manually creating calendar entries for weekly, bi-weekly, or daily recurring events, this tool processes structured data and automatically:

- Expands recurring event patterns (daily, weekly, bi-weekly, one-time)
- Integrates German holidays into the master calendar
- Generates high-quality visual calendar representations
- Creates sliding 7-day window visualizations for detailed weekly views
- Provides a web API for programmatic event submission

## Tech Stack

- **Python 3.x** - Core application logic
- **Flask** - Web framework for API endpoints
- **Pandas** - Event data processing and calendar generation
- **Matplotlib** - High-quality calendar visualizations
- **workalendar** - German holiday calendar integration
- **ThreadPoolExecutor** - Parallel processing for frame generation

## Repository Structure

```
weekly-calendar-planner/
├── main.py                 # Main application logic and visualization engine
├── app.py                  # Flask web server with API endpoints
├── events.csv              # Sample event data (your schedule input)
├── data.csv                # Alternative sample data format
├── requirements.txt        # Python dependencies
├── table.html              # HTML form for manual event entry
├── new_main.py             # Event data format documentation
├── test.py                 # Test utilities
├── testing.py              # Data processing utilities
├── dayereh.txt             # Sample numeric data
├── .gitignore              # Git ignore patterns
│
├── frames/                 # (Generated) Weekly 7-day sliding window PNGs
├── calendar.png            # (Generated) Main calendar visualization
├── extended_data.csv       # (Generated) Resolved recurring events
└── master_calendar.csv     # (Generated) Master calendar with holidays
```

## Setup & Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install flask pandas matplotlib workalendar click
```

## How to Run

### 1. Prepare Your Event Data

Create or modify `events.csv` with your schedule data. Required columns:
- `date start`, `date end` - Date range in DD/MM/YYYY format
- `type` - Event type (lecture, tutorial, assignment, exam, personal, work, self-study, leisure, other)
- `group` - Event category/group name
- `day` - Day of week for recurring events
- `daily`, `weekly`, `bi-weekly`, `one-time` - Recurrence flags (True/False)
- `name` - Event display name
- `time start`, `time end` - Times in HH:MM format
- `Status` - Active/inactive (True/False)
- `Location` - Event location (optional)
- `Additional Info` - Notes (optional)

See `events.csv` for a complete example.

### 2. Generate Calendar Visualizations

Run the main application from the repository root:

```bash
python main.py
```

This will:
- Read event data from `events.csv`
- Create a master calendar with German holidays
- Expand all recurring events across the date range
- Generate `calendar.png` with the full schedule visualization
- Create `frames/` directory with individual weekly PNG files
- Output `extended_data.csv` and `master_calendar.csv`

**Note:** Frame generation uses parallel processing and may take a few minutes depending on the date range.

### 3. Run Flask Web Server (Optional)

Start the API server for programmatic event submission:

```bash
python app.py
```

The server starts on `http://127.0.0.1:5000`

#### API Endpoint: POST /entry

Submit calendar entries as JSON:

```bash
curl -X POST http://127.0.0.1:5000/entry \
  -H "Content-Type: application/json" \
  -d '{"date":"2025-01-15","event":"Team Meeting","time":"14:00"}'
```

### 4. Manual Event Entry (Optional)

Open `table.html` in a web browser for a form-based event entry interface. The form provides dropdowns and inputs for all event fields with validation.

## Input Data Format

### CSV Structure

The application expects CSV files with the following columns:

| Column | Format | Description |
|--------|--------|-------------|
| date start | DD/MM/YYYY | Event start date |
| date end | DD/MM/YYYY | Event end date (for recurring events, this is the recurrence end) |
| type | string | Event category |
| group | string | Event group/subject |
| day | Day name | For recurring: Monday, Tuesday, etc. |
| daily | Boolean | True if event repeats daily |
| weekly | Boolean | True if event repeats weekly |
| bi-weekly | Boolean | True if event repeats every 2 weeks |
| one-time | Boolean | True if event occurs once |
| name | string | Display name for event |
| time start | HH:MM | Start time |
| time end | HH:MM | End time |
| Status | Boolean | True if event is active |
| To-Fill | Boolean | True if requires completion |
| Location | string | Event location |
| Additional Info | string | Notes or description |

**Example:**
```csv
date start,date end,type,group,day,daily,weekly,bi-weekly,one-time,name,time start,time end,Status,To-Fill,Location,Additional Info
7/4/2025,18/7/2025,lecture,Programming,Tuesday,False,True,False,False,Python Basics,10:00,12:00,True,False,Room 101,Introduction to Python
```

## Output Files

### Generated Visualizations

1. **calendar.png** - Full calendar visualization
   - Time-blocked schedule from 6:00 to 24:00
   - Color-coded by event group
   - Includes German holidays and weekends
   - Shows all days in the date range

2. **frames/*.png** - Weekly sliding windows
   - 7-day views with overlapping ranges
   - Detailed visualization for weekly planning
   - File naming: `calendar_YYYY-MM-DD_YYYY-MM-DD.png`

### Generated Data Files

1. **extended_data.csv** - All events with recurring patterns resolved
   - Each occurrence is a separate row
   - Single date (not date range)
   - Ready for visualization or export

2. **master_calendar.csv** - Master calendar reference
   - One row per day in the range
   - Includes: date, day name, holiday name (if any), weekend flag, off-day flag
   - Links to child events via index references

## Customization

### Adjust Visualization Hours

Edit `main.py` around line 492:

```python
draw_calendar(
    mc,
    extended_df,
    start_hour=6,    # Change start hour
    end_hour=24,     # Change end hour
    name_file="calendar.png",
)
```

### Change Holiday Calendar

Edit `main.py` around line 55 to use a different country's holidays:

```python
from workalendar.europe import Germany, France, Spain  # Import alternatives
cal = France()  # Change the calendar
```

### Modify Event Types

Edit `table.html` lines 66-79 to customize the event type dropdown options.

## Troubleshooting

### Import Errors

**Problem:** `ModuleNotFoundError: No module named 'flask'` (or pandas, matplotlib, etc.)

**Solution:** Install dependencies with `pip install -r requirements.txt`

### Flask Won't Start

**Problem:** Port 5000 already in use

**Solution:** 
- Kill the process using port 5000: `lsof -ti:5000 | xargs kill` (macOS/Linux)
- Or change the port in `app.py`: `app.run(host="127.0.0.1", port=8000)`

### Visualization Issues

**Problem:** Matplotlib backend errors or blank images

**Solution:**
- On Linux servers without display: `export MPLBACKEND=Agg` before running
- On macOS: Ensure you're not running in SSH without X11 forwarding
- Try: `matplotlib.use('Agg')` at the top of main.py

### CSV Parsing Errors

**Problem:** Date parsing errors or encoding issues

**Solution:**
- Ensure dates are in DD/MM/YYYY format
- Save CSV files with UTF-8 encoding
- Check for extra commas or missing columns
- Verify Boolean columns contain True/False (not 1/0 or yes/no)

### File Not Found

**Problem:** `FileNotFoundError: [Errno 2] No such file or directory: 'events.csv'`

**Solution:**
- Ensure you run `python main.py` from the repository root directory
- Verify `events.csv` exists in the same directory as `main.py`
- If using a different filename, update line 472 in `main.py`

### Memory Issues with Large Date Ranges

**Problem:** High memory usage or slow performance

**Solution:**
- Reduce the date range in your CSV data
- Limit the number of concurrent workers in `main.py` line 512: `num_workers = 2`
- Consider generating frames for specific date ranges only

## Notes

- The application uses German holidays via `workalendar.europe.Germany`
- Frame generation uses parallel processing (CPU count - 1 workers)
- Color assignment is persistent across runs using in-memory cache
- File paths are relative to the project directory (project-root-relative)
- Event types are flexible and can be customized in the data and HTML form
- The Flask server runs in debug mode by default (disable for production)

## Development Files

- `new_main.py` - Contains event data format documentation and field specifications
- `test.py` - Date iteration testing utility
- `testing.py` - Data parsing and processing utilities
- `dayereh.txt` - Sample numeric sequence data used for testing

These files represent development iterations and testing utilities retained for reference.
