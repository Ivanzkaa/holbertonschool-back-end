#!/usr/bin/python3
"""wrting  a python api script"""

import json
from requests import get


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = get('{}users/{}'.format(url, user_id)).json()

    all_emplyees = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks = get('{}todos?userId={}'.format(url, user_id)).json()
        for task in tasks:
            task_dict = {"task": task['title'],
                         "completed": task['completed'],
                         "username": username}
        all_emplyees[user_id] = task_dict
        filename = 'todo_all_employees.json'
        with open(filename, 'w') as file:
            json.dump(all_emplyees, file)
