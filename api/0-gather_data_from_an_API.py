#!/usr/bin/python3
"""
    python script that returns TODO list progress for a given employee ID
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    # Request user info by employee ID
    employee_id = argv[1]
    
    user_info_url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(employee_id)
    user_todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    
    # Request user info
    res_user_info = requests.get(user_info_url, verify=False)
    employee = json.loads(res_user_info.text)
    employee_name = employee.get("name")

    # Request user's TODO list
    res_user_todos = requests.get(user_todos_url, verify=False)
    employee_todos = json.loads(res_user_todos.text)

    # Dictionary to store task status in boolean format
    tasks = {dictionary.get("title"): dictionary.get("completed") for dictionary in employee_todos}

    # Return name, total number of tasks & completed tasks
    total_tasks = len(tasks)
    completed_tasks = [k for k, v in tasks.items() if v]
    
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))
    
    for task, completed in tasks.items():
        if completed:
            print("\t {}".format(task))
