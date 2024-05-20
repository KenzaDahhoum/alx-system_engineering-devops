#!/usr/bin/python3
"""Exports data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get('username')

    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_data = [todo for todo in todos_response.json() if todo.get('userId') == int(user_id)]

    json_data = {
        user_id: [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            } for task in todos_data
        ]
    }

    filename = f"{user_id}.json"
    with open(filename, mode='w') as f:
        json.dump(json_data, f)

    print(f"Data exported to {filename}")

