#!/usr/bin/python3
"""
    The code you provided is a Python script that retrieves information
    about a user's TODO list progress from a web API and saves it to a CSV file
"""


if __name__ == "__main__":
    import requests
    import sys
    import csv
    if len(sys.argv) != 2:
        exit()

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(sys.argv[1]))
    todos = todos.json()

    name = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                        .format(sys.argv[1]))
    name = name.json()
    name = name[0]["username"]

    file_name = "{}.csv".format(sys.argv[1])

    with open(file_name, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [sys.argv[1], name, todo['completed'], todo['title']])
