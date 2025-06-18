import os

tasks = []

def menu():
    print("\n       -> TO-DO LIST MENU <-     \n")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit\n")
   

def show():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{i}. {task['task']} [{status}]")

def addt():
    task_text = input("Enter the task: ")
    tasks.append({"task": task_text, "completed": False})
    print("Task added successfully.")

def mark_com():
    show_tasks()
    try:
        task_num=int(input("Enter task number to mark as completed: "))
        if 1<=task_num<=len(tasks):
            tasks[task_num-1]['completed']=True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def deletet():
    show()
    try:
        task_num=int(input("Enter task number to delete: "))
        if 1<=task_num<=len(tasks):
            deleted = tasks.pop(task_num-1)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def toapp():
    while True:
        menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            show()
        elif choice == '2':
            addt()
        elif choice == '3':
            mark_com()
        elif choice == '4':
            deletet()
        elif choice == '5':
            print("\nGoodbye! Your tasks were not saved.")
            break
        else:
            print("Invalid option. Please choose from 1 to 5.")

toapp()
