#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


def information_employee():
    """returns information about employees"""
    num = argv[1]  # python3 does not count as argument

    user_query = {'id': num}  # this is added as query parameter
    # that are appended to the endpoint URL
    response_1 = requests.get("https://jsonplaceholder.typicode.com/users",
                              params=user_query)  # endpoint URL

    todo_query = {'userId': num}  # match todo list with user specified
    response_2 = requests.get("https://jsonplaceholder.typicode.com/todos",
                              params=todo_query)

    user = response_1.json()  # .json() is a built in decoder
    # from request module, returning a list of dictionaries

    todo_list = response_2.json()

    employee_name = user[0].get('name')  # retrieve value from given key

    completed_tasks = 0
    total_tasks = 0
    completed_task_title = []

    for task in todo_list:
        if task.get('completed') is True:
            completed_task_title.append(task.get('title'))  # create list
            # from completed tasks
            completed_tasks += 1
        total_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_tasks, total_tasks))
    for title in completed_task_title:
        print('\t {}'.format(title))

if __name__ == "__main__":
    information_employee()
