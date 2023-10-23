#!/usr/bin/python3
"""
Script retrieves and displays information about an employee's
TODO list progress from REST API.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./0-gather_data_from_an_API.py employee_id")

    employee_id = sys.argv[1]

    # Make request to API to get employee's information
    user_info_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    base_url = 'https://jsonplaceholder.typicode.com/todos'
    query_param = f'?userId={employee_id}'
    todo_url = base_url + query_param
    try:
        user_info_response = requests.get(user_info_url)
        todo_response = requests.get(todo_url)

        user_info = user_info_response.json()
        todos = todo_response.json()

        # Calculate number of completed and total tasks
        total_tasks = len(todos)
        completed_tasks = sum(1 for task in todos if task['completed'])

        # Display employee's TODO list progress
        print(f"Employee {user_info['name']} is done with tasks"
              f" ({completed_tasks}/{total_tasks}):")
        for task in todos:
            if task['completed']:
                print(f"\t {task['title']}")
    except requests.exceptions.RequestException as e:
        sys.exit(f"An error occurred: {e}")
