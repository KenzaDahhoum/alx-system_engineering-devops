#!/usr/bin/python3
"""For a given employee ID, exports information about
their TODO list progress to a CSV file"""

import csv
import requests
import sys

def fetch_employee_data(employee_id):
    """Fetch employee username and TODO list data from the API."""
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if user_response.status_code != 200:
        return None, []

    username = user_response.json().get('username')

    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_data = [todo for todo in todos_response.json() if todo.get('userId') == employee_id]

    return username, todos_data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    username, todos_data = fetch_employee_data(employee_id)
    if username is None:
        print("User not found")
        sys.exit(1)

    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            writer.writerow([employee_id, username, task.get('completed'), task.get('title')])
    
    print(f"Data exported to {csv_filename}")

