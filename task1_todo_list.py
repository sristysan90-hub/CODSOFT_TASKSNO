"""CodSoft Task 1 - To-Do List (command line, saves tasks to a JSON file)."""
import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.")
        return
    print("\nYour tasks:")
    for i, t in enumerate(tasks, 1):
        mark = "[x]" if t["done"] else "[ ]"
        print(f"  {i}. {mark} {t['title']}")


def get_number(prompt, tasks):
    try:
        n = int(input(prompt))
        if 1 <= n <= len(tasks):
            return n - 1
    except ValueError:
        pass
    print("Invalid task number.")
    return None


def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Mark task as done")
        print("5. Delete task")
        print("6. Exit")
        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Task title: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Title cannot be empty.")
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                idx = get_number("Task number to update: ", tasks)
                if idx is not None:
                    new_title = input("New title: ").strip()
                    if new_title:
                        tasks[idx]["title"] = new_title
                        save_tasks(tasks)
                        print("Task updated.")
        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                idx = get_number("Task number to mark done: ", tasks)
                if idx is not None:
                    tasks[idx]["done"] = True
                    save_tasks(tasks)
                    print("Task marked as done.")
        elif choice == "5":
            show_tasks(tasks)
            if tasks:
                idx = get_number("Task number to delete: ", tasks)
                if idx is not None:
                    removed = tasks.pop(idx)
                    save_tasks(tasks)
                    print(f"Deleted: {removed['title']}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
