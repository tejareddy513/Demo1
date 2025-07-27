import argparse
import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return f.read().splitlines()

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        f.write("\n".join(tasks))

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Added: '{task}'")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("📋 Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"❌ Removed: '{removed}'")
    except IndexError:
        print("⚠️ Invalid task number.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple To-Do CLI app")
    parser.add_argument("command", choices=["add", "list", "remove"])
    parser.add_argument("data", nargs="?", help="Task or task number")

    args = parser.parse_args()

    if args.command == "add" and args.data:
        add_task(args.data)
    elif args.command == "list":
        list_tasks()
    elif args.command == "remove" and args.data and args.data.isdigit():
        remove_task(int(args.data))
    else:
        print("⚙️ Usage examples:")
        print("  python todo.py add 'Buy milk'")
        print("  python todo.py list")
        print("  python todo.py remove 1")
