import sys
import datetime

def extract_logs(log_file_path, target_date_str):
    """
    Extracts log entries from a large log file for a specific date.

    Args:
        log_file_path (str): Path to the log file.
        target_date_str (str): Target date in YYYY-MM-DD format.
    """
    try:
        target_date = datetime.datetime.strptime(target_date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
        return

    try:
        with open(large_file_path, 'r', encoding='utf-8') as log_file:
            for line in log_file:
                try:
                    log_date_str = line[:10]  # Extract date part from the line
                    log_date = datetime.datetime.strptime(log_date_str, '%Y-%m-%d').date()

                    if log_date == target_date:
                        print(line.strip())  # Print the log entry
                except ValueError:
                    # Handle lines that don't match the expected format
                    pass #or print a warning, or log it to a file
    except FileNotFoundError:
        print(f"Error: Log file not found at {large_file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if _name_ == "_main_":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    target_date_str = sys.argv[1]
    log_file_path = "logfile.log" #replace with your log file path

    extract_logs(log_file_path, target_date_str)