#!/usr/bin/python3
"""
    script that, using this https://jsonplaceholder.typicode.com/, for a given
    employee ID, returns information about his/her TODO list progress.
"""


if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) != 2:
        exit()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}&completed=true"
        .format(sys.argv[1]))
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(sys.argv[1]))
    name = name.json()
    name = name[0]["name"]
    todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(sys.argv[1]))
    todo = todo.json()
    todo = len(todo)
    todos = todos.json()
    todo_list = []

    for task in todos:
        todo_list.append("\t {}".format(task["title"]))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(todos), todo))
    for i in todo_list:
        print(i)
