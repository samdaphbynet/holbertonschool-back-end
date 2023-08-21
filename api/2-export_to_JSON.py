#!/usr/bin/python3
"""
    The code block `if __name__ == "__main__":` is a common idiom in Python
    that allows a module to be
    run as a standalone script or imported by other modules.
"""

if __name__ == "__main__":
    import sys
    import requests
    import json
    if len(sys.argv) != 2:
        exit()

    # The code block you provided is making HTTP
    # requests to two different endpoints and processing
    # the response data.
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1]))
    todos = todos.json()

    name = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                        .format(sys.argv[1]))
    name = name.json()[0]["username"]

    file_name = "{}.json".format(sys.argv[1])

    # The code block you provided is creating a dictionary called `result`
    # and initializing it as an
    # empty dictionary. Then, it adds a key-value pair to the `result`
    # dictionary, where the key is
    # `sys.argv[1]` (the command-line argument passed to the script)
    # and the value is an empty list.
    result = {}
    result[sys.argv[1]] = []

    for todo in todos:
        result[sys.argv[1]].append(
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": name
            })

    with open(file_name, 'w') as json_file:
        json.dump(result, json_file)
