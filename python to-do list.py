def display_menu():
    print("TO-DO LIST: all tasks are signs of progress!!!")
    print("Menu:")
    print("1. Add a Task")
    print("2. View all the Tasks")
    print("3. Mark as completed")
    print("4. Exit the program")

def add_task(t1):
    task = input("Enter task description: ")
    t1.append(task)
    print("Task added successfully!!!") 
    
def view_tasks(t1):
    print("\nTasks:")
    for i, task in enumerate(t1, start=1):
        print(f"{i}. {task}")

def mark_task_done(t1):
    if not t1:
        print("No tasks left to be marked as done.")
        return


    view_tasks(t1)  # Display tasks with indices
    index = int(input("Enter task index to be marked: ")) - 1


    if 0 <= index < len(t1):
        removed_task = t1.pop(index)
        print(f"Task '{removed_task}' marked as done and removed.")
    else:
        print("Invalid task index.")

def main():
    tasks = []  # Initialize an empty list to store tasks


    while True:
        display_menu()


        choice = input("Enter the choice: ")


        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + '\n')
            f.show()


def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def main():
    tasks = load_tasks()  # Load tasks from file


    while True:
        # Don't forget to save tasks before exiting
        save_tasks(tasks) 

def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append(task)
    print("Task added successfully!")


def view_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return


    view_tasks(tasks)
    index = int(input("Enter task index to mark as done: ")) - 1


    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' marked as done and removed.")
    else:
        print("Invalid task index.")


def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + '\n')


def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def main():
    tasks = load_tasks()


    while True:
        display_menu()


        choice = input("Enter the choice: ")


        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Exiting.")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
