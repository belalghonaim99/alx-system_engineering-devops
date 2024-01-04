#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed = []  # Define the 'completed' list

    for todo in todos:
        if todo.get("completed"):
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(completed), len(todos)))

    for task_title in completed:
        print("\t {}".format(task_title))
