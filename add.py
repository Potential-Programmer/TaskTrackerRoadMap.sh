import time
import json
def add(previous_tasks:list=[]):
    print("Adding a task...")
    task = input("Enter the task: ")
    taskF = {"id": len(previous_tasks)+1, "task": task, "status": "todo", "created_at": time.strftime("%d/%m/%Y %H:%M:%S"),"updated_at": time.strftime("%d/%m/%Y %H:%M:%S")}
    previous_tasks.append(taskF)

    with open("tasks.json", "w") as file:
        file.write(json.dumps(previous_tasks, indent=4))
    print("Task added successfully! ID:{}  Task: {}".format(len(previous_tasks), task))