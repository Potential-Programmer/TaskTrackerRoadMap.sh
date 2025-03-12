"""
10/03/2025
Author and Owner: "Jasser Ahmed Bassuny"
Description: "This is a simple python task tracker application that allows the user to add, delete, and view tasks on CLI."
Version: 0.1
"""
import json
try:
    with open("tasks.json", "r") as file:
        tasks = file.read()
        tasks = json.loads(tasks)
        print(type(tasks))

except FileNotFoundError:
    tasks = []
    with open("tasks.json", "w") as file:
        file.write("[]")

command = input("Enter a command: ")
split = command.split(" ")

while True:
    if command == "add":
        import add
        add.add(tasks)
    #elif command == "delete":
    #    import delete
    elif "view" == split[0]:
        import view
        if len(split) == 1:
            view.view(tasks)
        else:
            view.view(tasks, int(split[1]))
    elif command == "exit":
        Confirm = input("Are you sure you want to exit? Y/N: ")
        if Confirm == "Y":
            break
        continue

    else:
        print("Invalid command!")
    command = input("Enter a command: ")
    split = command.split(" ")
