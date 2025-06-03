import json
import os

FILENAME = "tasks.json"
tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            tasks = json.load(file)

# Save tasks to file
def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Show all tasks
def view_tasks():
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task['completed'] else "✗"
        print(f"{i}. [{status}] {task['title']} | Category: {task['category']} | Priority: {task['priority']}")

# Add a new task
def add_task():
    title = input("Enter task title: ")
    category = input("Enter category (e.g., Work, Study): ")
    priority = input("Enter priority (High/Medium/Low): ")
    task = {
        "title": title,
        "category": category,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

# Mark a task as complete
def mark_complete():
    view_tasks()
    try:
        choice = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= choice < len(tasks):
            tasks[choice]['completed'] = True
            save_tasks()
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Edit a task
def edit_task():
    view_tasks()
    try:
        index = int(input("Enter task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            title = input("New title (leave blank to keep current): ")
            category = input("New category (leave blank to keep current): ")
            priority = input("New priority (High/Medium/Low, leave blank to keep current): ")

            if title:
                tasks[index]['title'] = title
            if category:
                tasks[index]['category'] = category
            if priority:
                tasks[index]['priority'] = priority
            save_tasks()
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks()
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Exit")

# Run the app
load_tasks()
while True:
    menu()
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        edit_task()
    elif choice == '5':
        delete_task()
    elif choice == '6':
        print("Goodbye! 👋")
        break
    else:
        print("Invalid option. Please choose a number from 1 to 6.")
