#!/usr/bin/python3
"""Python script that returns information about employees"""

import requests
import sys


if __name__ == '__main__':
    employee_Id = sys.argv[1]
    base_Url = "https://jsonplaceholder.typicode.com/users"
    url = base_Url + "/" + employee_Id

    response = requests.get(url)
    username = response.json().get('username')

    to_do_Url = url + "/todos"
    response = requests.get(to_do_Url)
    tasks = response.json()

    with open('{}.csv'.format(employee_Id), 'w') as file:
        for tsk in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_Id, username, tsk.get('completed'),
                               tsk.get('title')))
