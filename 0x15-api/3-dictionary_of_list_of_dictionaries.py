#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    # Define base URL for JSONPlaceholder API
    base_url = 'https://jsonplaceholder.typicode.com/'

    # Create dictionary to store tasks by user ID
    tasks_by_user = {}

    # Fetch all users
    users_response = requests.get(base_url + 'users')
    users = users_response.json()

    # Iterate through each user and fetch their tasks
    for user in users:
        user_id = user['id']
        username = user['username']

        # Fetch tasks for current user
        tasks_response = requests.get(base_url + 'todos', params={'userId': user_id})
        tasks = tasks_response.json()

        # Create list of tasks for current user
        user_tasks = [{'username': username, 'task': task['title'], 'completed': task['completed']} for task in tasks]

        # Add user tasks to dictionary
        tasks_by_user[user_id] = user_tasks

    # Save tasks data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(tasks_by_user, json_file)
