"""
10/03/2025
Author and Owner: "Jasser Ahmed Bassuny"
Description: "This is a simple python task tracker application that allows the user to add, delete, and view tasks on CLI."
Version: 0.1
"""
try:
    with open("tasks.json", "r") as file:
        tasks = file.read()
        if tasks == "":
            tasks = []

except FileNotFoundError:
    tasks = []
    with open("tasks.json", "w") as file:
        file.write("[]")

command = input("Enter a command: ")
while True:
    if command == "add":
        import add
        add.add(tasks)
    #elif command == "delete":
    #    import delete
    #elif command == "view":
    #    import view
    elif command == "exit":
        Confirm = input("Are you sure you want to exit? Y/N: ")
        if Confirm == "Y":
            break
        continue

    else:
        print("Invalid command!")
    command = input("Enter a command: ")
