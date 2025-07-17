from file_handler import save_tasks
from task import Task
from datetime import datetime

def add_task(task_list):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    priority = int(input("Enter task priority (low=3, medium=2, high=1): "))
    deadline = input("Enter task deadline (YYYY-MM-DD): ")

    task = Task(title, description, priority, deadline)

    task_list.add(task)
    save_tasks(task_list.all())
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"\nTask {i}:\n{task}")

def delete_task(task_list):
    view_tasks(task_list.all())
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(task_list.all()):
        task_list.remove(task_index)
        save_tasks(task_list.all())
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def sort_tasks(task_list):
    print("Sort tasks by:")
    print("1. Priority")
    print("2. Deadline")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        task_list.sort(key=lambda x: x.priority)
        save_tasks(task_list.all())
        print("Tasks sorted by priority")
    elif choice == "2":
        task_list.sort(key=lambda x: x.deadline)
        save_tasks(task_list.all())
        print("Tasks sorted by deadline.")
    else:
        print("Invalid choice.")

def show_high_priority_tasks(tasks):
    high_priority_tasks = [task for task in tasks if task.priority == 1]
    if not high_priority_tasks:
        print("No high priority tasks available.")
    else:
        print("High Priority Tasks:")
        for task in high_priority_tasks:
            print(f"\n {task}")

def get_overdue_tasks(tasks):
    today = datetime.today().strftime("%Y-%m-%d")
    for task in tasks:
        if task.deadline < today:
            yield task

def show_overdue_tasks(tasks):
    print("Overdue Tasks:")
    found = False
    for task in get_overdue_tasks(tasks):
        print(f"\n{task}")
        found = True
    if not found:
        print("No overdue tasks found.")