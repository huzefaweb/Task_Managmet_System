from multiprocessing import Process

def anaylze_task(tasks):
    print(f"Analyzing {len(tasks)} tasks...")
    for task in tasks:
        print(f"Task: {task}")

def run_analysis(task_list):
    tasks = task_list.all()
    p = Process(target=anaylze_task, args=(tasks,))
    p.start()
    p.join()