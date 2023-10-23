#!/usr/bin/python3
"""
Script retrieves and exports information about an employee's TODO list progress
from a REST API in JSON format.
"""

import sys
import requests
import json

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./2-export_to_JSON.py employee_id")

    employee_id = sys.argv[1]

    # Make request to API to get employee's information
    user_info_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = (f'https://jsonplaceholder.typicode.com/todos'
                f'?userId={employee_id}')

    try:
        user_info_response = requests.get(user_info_url)
        todo_response = requests.get(todo_url)

        user_info = user_info_response.json()
        todos = todo_response.json()

        # Create JSON data structure
        json_data = {user_info['id']: [
            {"task": task['title'], "completed": task['completed'],
             "username": user_info['username']} for task in todos]}

        # Create JSON file for user
        json_filename = f'{employee_id}.json'

        with open(json_filename, 'w') as jsonfile:
            json.dump(json_data, jsonfile)

        print(f"Data exported to {json_filename}")
    except requests.exceptions.RequestException as e:
        sys.exit(f"An error occurred: {e}")
