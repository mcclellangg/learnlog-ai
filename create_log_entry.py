"""
create_log_entry.py

Generates a new daily markdown log file using a predefined template.

This script reads from a template file ("template.md"), inserts the current
date and time (in EST, formatted as MM-DD-YYYY and HH:MM:SS AM/PM), and saves
the new log entry in the "logs" directory. The filename is based on the date,
and the script prevents overwriting existing logs by asserting nonexistence.

Intended to be called via a PowerShell wrapper or run manually.

Example:
    python create_log_entry.py
"""

from datetime import datetime, timezone, timedelta
import os

# CONFIG
TEMPLATE_FILEPATH = ".\\template.md"
LOGS_DIR = ".\\logs"

# MAIN
def main():
    # Define EST timezone manually (UTC-5)
    est = timezone(timedelta(hours=-5))
    now = datetime.now(est)

    date_str = now.strftime("%m-%d-%Y")
    time_str = now.strftime("%I:%M:%S %p")
    filename = f"{date_str}.md"
    filepath = os.path.join(LOGS_DIR, filename)

    # Assert the file does not already exist
    assert not os.path.exists(filepath), f"Log file already exists: {filepath}"
    
    try:
        with open(TEMPLATE_FILEPATH, "r", encoding="utf-8") as template_file:
            content = template_file.read()
        
        content = content.replace("MM-DD-YYYY", date_str)
        content = content.replace("time:", f"time: {time_str}")

        with open(filepath, "w", encoding="utf-8") as log_file:
            log_file.write(content)

        print(f"Created new log: {filepath}")

    except Exception as e:
        print(f"Error creating log: {e}")

if __name__ == "__main__":
    main()