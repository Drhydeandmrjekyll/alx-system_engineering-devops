#!/usr/bin/python3
"""
Script retrieves and displays information about an employee's
TODO list progress from a REST API.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./0-gather_data_from_an_API.py employee_id")

    employee_id = sys.argv[1]

    try:
        base_url = 'https://jsonplaceholder.typicode.com/users/'
        user_info_url = f'{base_url}{employee_id}'
        user_info_response = requests.get(user_info_url)
        todo_response = requests.get(f'https://jsonplaceholder.typicode.com'
                                     f'/todos?userId={employee_id}')

        user_info = user_info_response.json()
        todos = todo_response.json()

        # Calculate number of completed and total tasks
        total_tasks = len(todos)
        completed_tasks = sum(1 for task in todos if task['completed'])

        # Display employee's TODO list progress
        print(f"Employee {user_info['username']} is done with tasks"
              f"({completed_tasks}/{total_tasks}):")
        for task in todos:
            if task['completed']:
                print(f"\t{task['title']}")
    except requests.exceptions.RequestException as e:
        sys.exit(f"An error occurred: {e}")
