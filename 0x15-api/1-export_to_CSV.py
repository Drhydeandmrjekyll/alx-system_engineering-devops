#!/usr/bin/python3
"""
Script retrieves and exports information about an employee's TODO list progress from a REST API in CSV format.
"""

import sys
import requests
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./1-export_to_CSV.py employee_id")

    employee_id = sys.argv[1]

    # Make request to API to get employee's information
    user_info_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        user_info_response = requests.get(user_info_url)
        todo_response = requests.get(todo_url)

        user_info = user_info_response.json()
        todos = todo_response.json()

        # Create CSV file for user
        csv_filename = f'{employee_id}.csv'

        with open(csv_filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            
            for task in todos:
                csvwriter.writerow([user_info['id'], user_info['username'], task['completed'], task['title']])
                
        print(f"Data exported to {csv_filename}")
    except requests.exceptions.RequestException as e:
        sys.exit(f"An error occurred: {e}")
