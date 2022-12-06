#!/usr/bin/python3
"""writing a script using restapi
for information about emplyees"""


from requests import get
from sys import argv


if __name__ == "__main__":
    employee_data = int(argv[1])
    user = get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_data)).json()
    todo = get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_data)).json()

    tasks_done = []
    for task in todo:
        if task.get('completed') is True:
            tasks_done.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(user.get('name'), len(tasks_done), len (todo)))

    for done in tasks_done:
        print("\t {}".format(done))
