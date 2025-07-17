import threading

def reminder(task_list):
    def remind():
            print(f"Reminder: You have {len(task_list.all())} tasks to complete!")

    reminder_thread = threading.Thread(target=remind)
    reminder_thread.start()