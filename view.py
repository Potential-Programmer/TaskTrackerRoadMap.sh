
def view(tasks:list=[], n:int=0):
    if tasks == []:
        print("No tasks to display!")
    elif n != 0:
        for task in tasks:
            if n == task["id"]:
                x = len(f"{task["id"]}  -" + " "*int(len(task["task"])/2) + f"{task["task"]}" + " "*int(len(task["task"])/4) + " -" + " "*int(len(task["status"])/2) + f"{task["status"]}" + " "*int(len(task["status"])/2) + f"- {task["created_at"]} - {task["updated_at"]}")
                print("-"*x)
                print("ID -" + " "*int(len(task["task"])/2) + "Task" + " "*int(len(task["task"])/2) + "-" + " "*int(len(task["status"])/2) + "Status" + " "*int(len(task["status"])/2) + "-       Created At    -      Updated At")
                print(f"{task["id"]}  -" + " "*int(len(task["task"])/2) + f"{task["task"]}" + " "*int(len(task["task"])/4) + " -" + " "*int(len(task["status"])/2) + f"{task["status"]}" + " "*int(len(task["status"])/2) + f"- {task["created_at"]} - {task["updated_at"]}")
                print("-"*x)
                print()
                break
    else:
        for task in tasks:
            x = len(f"{task["id"]}  -" + " "*int(len(task["task"])/2) + f"{task["task"]}" + " "*int(len(task["task"])/4) + " -" + " "*int(len(task["status"])/2) + f"{task["status"]}" + " "*int(len(task["status"])/2) + f"- {task["created_at"]} - {task["updated_at"]}")
            print("-"*x)
            print("ID -" + " "*int(len(task["task"])/2) + "Task" + " "*int(len(task["task"])/2) + "-" + " "*int(len(task["status"])/2) + "Status" + " "*int(len(task["status"])/2) + "-       Created At    -      Updated At")
            print(f"{task["id"]}  -" + " "*int(len(task["task"])/2) + f"{task["task"]}" + " "*int(len(task["task"])/4) + " -" + " "*int(len(task["status"])/2) + f"{task["status"]}" + " "*int(len(task["status"])/2) + f"- {task["created_at"]} - {task["updated_at"]}")
            print("-"*x)
            print()

    
tasks = [{"id": 1,"task": "hello","status": "todo","created_at": "11/03/2025 18:49:49","updated_at": "11/03/2025 18:49:49"},
         {"id": 2,"task": "hello","status": "todo","created_at": "11/03/2025 18:49:49","updated_at": "11/03/2025 18:49:49"}
         ]

#view(tasks,2)
