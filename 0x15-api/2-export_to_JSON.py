#!/usr/bin/python3
"""Exports data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]

    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    user_data = user_response.json()

    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_data = todos_response.json()

    todo_user = {}
    task_list = []

    for task in todos_data:
        if task.get('userId') == int(userId):
            task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user_data.get('username')
            }
            task_list.append(task_dict)

    todo_user[userId] = task_list

    filename = f"{userId}.json"
    with open(filename, mode='w') as f:
        json.dump(todo_user, f)

