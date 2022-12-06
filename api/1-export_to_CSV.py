#!/usr/bin/python3
"""wrting an api script"""


import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    users = get('{}users/{}'.format(url, user_id)).json()
    username = users.get('username')
    tasks = get('{}todo?userId={}'.format(url, user_id)).json()
    with open("{}.csv".format(user_id), 'wt') as file:
        write_file = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            write_file.writerow([int(user_id), username,
                                 task.get('completed'), task.get('title')])
