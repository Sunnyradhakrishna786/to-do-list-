

def display_menu():
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            print("\nYour tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task.strip()}")
        else:
            print("\nNo tasks found.")

def add_task():
    task = input("\nEnter your task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("\nTask added!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("\nTask deleted!")
        else:
            print("\nInvalid task number.")
    except ValueError:
        print("\nInvalid input.")

def main():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-4): ")
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("\nExiting. Goodbye!")
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()
