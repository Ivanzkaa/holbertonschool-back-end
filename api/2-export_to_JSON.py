#!/usr/bin/python3
"""wrting  a python api script"""


import json
from requests import get
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    users = get('{}users/{}'.format(url, user_id)).json()
    username = users.get('username')
    tasks = get('{}todo?userId={}'.format(url, user_id)).json()

    list_of_task = []
    for task in tasks:
        task_dict = {"task": task['title'],
                     "completed": task['completed'],
                     "username": username}

        list_of_task.append(task_dict)
        data = {str(user_id): list_of_task}
        filename = '{}.json'.format(user_id)
        with open(filename, 'w') as file:
            json.dump(data, file)
