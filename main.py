# Task Manager Application

from file_handler import load_tasks
from task_manager import add_task, view_tasks, delete_task, sort_tasks, show_high_priority_tasks, show_overdue_tasks
from task_list import TaskList
from threads_utils import reminder
from process_utils import run_analysis

def main():

    tasks = load_tasks()
    task_list = TaskList(tasks) # Initialize TaskList with loaded tasks
    
    while True:
        reminder(task_list)  # Start the reminder thread
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Run Analysis")
        print("5. Sort Tasks")
        print("6. Show High Priority Tasks")
        print("7. Show Overdue Tasks")
        print("8. Exit")

        choice = input("Enter your choice(1-8): ")

        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            delete_task(task_list)      
        elif choice == "4":
            run_analysis(task_list)
        elif choice == "5":
            sort_tasks(task_list)
        elif choice == "6":
            show_high_priority_tasks(task_list.all())
        elif choice == "7":
            show_overdue_tasks(task_list.all()) 
        elif choice == "8":
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()