## User-Friendly: Prompts the user to input the target date interactively.

Output: Saves the retrieved logs to a file named output/output_YYYY-MM-DD.txt.

## Prerequisites
Python 3.x

A large log file (large_log_file.txt) with logs sorted by timestamp.

### How to Use
Save the Script:

Save the script as log_retrieval.py.

## Prepare the Log File:

Ensure the log file (large_log_file.txt) is in the same directory as the script.

The log file must be sorted by timestamp for the binary search to work correctly.

## Run the Script:

Open a terminal or command prompt.

Navigate to the directory where the script and log file are located.

## Run the script:

bash
Copy
python log_retrieval.py
Enter the Target Date:

The script will prompt you to enter the target date in YYYY-MM-DD format:

Copy
Enter the target date (YYYY-MM-DD):
Enter the date (e.g., 2024-12-01) and press Enter.

## Check the Output:

The script will extract all logs for the specified date and save them to output/output_YYYY-MM-DD.txt.

A confirmation message will be displayed:

Copy
Logs for 2024-12-01 have been saved to output/output_2024-12-01.txt
Example
Input:
Log file (large_log_file.txt):

Copy
2024-12-01 14:23:45 INFO User logged in  
2024-12-01 14:24:10 ERROR Failed to connect to the database  
2024-12-02 09:15:30 WARN Disk space running low  
User input:

Copy
Enter the target date (YYYY-MM-DD): 2024-12-01
Output:
File output/output_2024-12-01.txt:

Copy
2024-12-01 14:23:45 INFO User logged in  
2024-12-01 14:24:10 ERROR Failed to connect to the database  
Confirmation message:

Copy
Logs for 2024-12-01 have been saved to output/output_2024-12-01.txt
Notes
File Sorting: The log file must be sorted by timestamp for the binary search to work correctly.

Output Directory: The script creates an output directory if it doesn't already exist.

Error Handling: If the user enters an invalid date format, the script will display an error message and exit.

## Code Overview
Key Functions:
binary_search(file, target_date, start, end):

Performs binary search to find the start or end position of logs for the target date.

extract_logs(input_file, target_date, output_file):

Extracts logs for the target date and saves them to the output file.

main():

Prompts the user for the target date, validates the input, and calls the extraction function.

## Performance
### Time Complexity: 
O(log N)
O(logN) for binary search, where N
N is the file size in bytes.

Memory Usage: Minimal, as the file is processed in chunks.

## Troubleshooting
Script Doesn't Ask for Target Date:

Ensure you are running the script interactively (e.g., python log_retrieval.py).

If using an IDE, make sure it supports interactive input.

## No Output File:

Check if the log file exists and is named large_log_file.txt.

Ensure the log file is sorted by timestamp.

## Invalid Date Format:

Enter the date in YYYY-MM-DD format (e.g., 2024-12-01).
