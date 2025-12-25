# Weekly Calendar Planner App

**Project Type:** Personal Project  
**Primary Stack:** Python/Flask

## Description

This is a personal weekly calendar planner application built with Flask. The application allows users to create, manage, and visualize weekly schedules with a calendar interface. It includes features for managing events, generating calendar views, and exporting data.

## Tech Stack

- Python 3.x
- Flask (web framework)
- Pandas (data handling)
- Matplotlib (visualization)
- workalendar (holiday handling)

## Folder Structure

```
weekly planner/
├── app.py                  # Flask web application server
├── main.py                 # Main application logic
├── new_main.py             # Updated main application
├── test.py                 # Test script
├── testing.py              # Testing utilities
├── data.csv                # Calendar data
├── extended_data.csv       # Extended calendar data
├── master_calendar.csv     # Master calendar file
├── calendar.png            # Calendar visualization
├── table.html              # HTML table output
├── dayereh.txt             # Additional data file
├── frames/                 # Output frames directory
└── README.md               # This file
```

## Setup / Installation

Install required dependencies:
```bash
pip install flask pandas matplotlib workalendar
```

Or using requirements file:
```bash
pip install -r requirements.txt
```

## How to Run

### Run Flask Web Server
```bash
cd "weekly planner"
python app.py
```

The server will start on `http://127.0.0.1:5000`

### Run Main Application
```bash
python main.py
```

Or the updated version:
```bash
python new_main.py
```

### Test the Application
```bash
python test.py
```

## Inputs/Outputs

**Inputs:**
- `data.csv` - Initial calendar data
- `extended_data.csv` - Extended event data
- `master_calendar.csv` - Master calendar entries
- `dayereh.txt` - Configuration or additional data

**Outputs:**
- `calendar.png` - Generated calendar visualization
- `table.html` - HTML table with calendar data
- `frames/` - Directory containing generated frame images
- Web interface accessible via Flask server

## API Endpoints

### POST /entry
- Receives calendar entry data as JSON
- Processes and stores the entry
- Returns confirmation

Example:
```bash
curl -X POST http://127.0.0.1:5000/entry \
  -H "Content-Type: application/json" \
  -d '{"date":"2025-01-15","event":"Meeting"}'
```

## Notes

- The application manages weekly calendar planning and visualization
- All file paths are relative to the project directory
- Multiple Python files suggest iterative development (main.py, new_main.py)
- Flask server runs in debug mode by default
- Uses German holidays via workalendar.europe.Germany

## Troubleshooting

- If Flask doesn't start, check port 5000 is available
- If you get import errors: `pip install flask pandas matplotlib workalendar`
- For visualization issues, ensure matplotlib backend is properly configured
- If CSV files are not found, verify you're running from the project directory
- For encoding issues with CSV files, check file encoding (UTF-8 recommended)
