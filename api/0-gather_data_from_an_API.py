#!/usr/bin/python3
"""
    script that, using this https://jsonplaceholder.typicode.com/, for a given
    employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_todo(employee_id):
    # Fetch user data
    usr_response = requests.get
    (f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    usr_data = usr_response.json()

    # Fetch user's todos
    todo_response = requests.get
    (f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todo_data = todo_response.json()

    # Calculate the number of completed tasks
    com_task = [task['title'] for task in todo_data if task['completed']]
    num_com_task = len(com_task)
    total_num_task = len(todo_data)

    print(f"Employee {usr_data['name']} is done with tasks\
          ({num_com_task}/{total_num_task}):")

    # Print titles of completed tasks
    for task in com_task:
        print(f"\t{task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo(employee_id)
