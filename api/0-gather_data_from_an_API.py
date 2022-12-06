#!/usr/bin/python3
"""writing a script using restapi
for information about emplyees"""


from requests import get
from sys import argv


if __name__ == "__main__":
    """returning the infromation about the employees"""
    EMPLOYEE_NAME = ""
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    tasks = []
    todo = get('https://jsonplaceholder.typicode.com/todos/')
    user = get('https://jsonplaceholder.typicode.com/user/')
    data = todo.json()
    data_2 = user.json()

    for name_info in data_2:
        if name_info.get('id') == int(argv[1]):
            EMPLOYEE_NAME = name_info.get('name')

    for id_info in data:
        if id_info.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1

        if id_info.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            tasks.append(id_info.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          TOTAL_NUMBER_OF_TASKS, NUMBER_OF_DONE_TASKS))
