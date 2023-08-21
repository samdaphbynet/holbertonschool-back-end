#!/usr/bin/python3
"""
    Using what you did in the task #0, extend your Python script
    to export data in the JSON format.
"""

if __name__ == "__main__":
    import requests
    import json

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()

    result = {}

    for usr in users:
        todos = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}"
            .format(usr["id"]))
        todos = todos.json()
        result[usr["id"]] = []

        for todo in todos:
            result[usr["id"]].append(
                {
                    "username": usr["username"],
                    "task": todo["title"],
                    "completed": todo["completed"]
                })

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(result, json_file)
