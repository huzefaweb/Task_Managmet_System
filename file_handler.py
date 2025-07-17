import json
import os
from task import Task

data_file = "data/tasks.json"

def load_tasks():
    if not os.path.exists(data_file):
        return []
    try:
        with open(data_file, 'r') as file:
            tasks= json.load(file)
            tasks = [Task(**task) for task in tasks]  # Convert dicts to Task objects
            return tasks
    except json.JSONDecodeError:
        print("Error reading tasks file. Starting with an empty task list.")
        return []

def save_tasks(tasks):
    os.makedirs(os.path.dirname(data_file), exist_ok=True)
    with open(data_file, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)
