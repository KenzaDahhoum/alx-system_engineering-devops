#!/usr/bin/python3
"""Exports data in the CSV format"""

import csv
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
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

    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            writer.writerow([user_id, username, str(task.get('completed')), task.get('title')])
    
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    main()

