import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_name = os.path.join(BASE_DIR, "todo_list.json")


def load_task():

    try:

        with open(file_name, "r") as file:
            return json.load(file)

    except:

        return {"tasks": []}


def save_task(tasks):

    try:

        with open(file_name, "w") as file:

            json.dump(tasks, file, indent=4)

    except Exception as e:

        print("Error:", e)


def view_task(tasks):

    print()

    task_list = tasks["tasks"]

    if len(task_list) == 0:

        print("Empty. No task to display.")

    else:

        print("Your To-Do List:")

        for idx, task in enumerate(task_list):

            status = (
                "[completed]"
                if task["complete"]
                else "[pending]"
            )

            print(
                f"{idx+1}. "
                f"{task['description']} | "
                f"{status} | "
                f"Priority: {task['priority']} | "
                f"Due: {task['due_date']}"
            )


def create_task(tasks):

    description = input(
        "Enter task description: "
    ).strip()

    priority = input(
        "Enter priority (low/medium/high): "
    ).strip().lower()

    due_date = input(
        "Enter due date (YYYY-MM-DD): "
    ).strip()

    if description:

        tasks["tasks"].append(
            {
                "description": description,
                "complete": False,
                "priority": priority,
                "due_date": due_date
            }
        )

        save_task(tasks)

        print("Task added.")

    else:

        print("Description cannot be empty.")


def marks_as_completed(tasks):

    view_task(tasks)

    try:

        task_number = int(
            input(
                "\nEnter task number to mark complete: "
            ).strip()
        )

        if 1 <= task_number <= len(tasks["tasks"]):

            tasks["tasks"][task_number - 1][
                "complete"
            ] = True

            save_task(tasks)

            print("Task marked as completed.")

        else:

            print("Invalid task number.")

    except Exception as e:

        print(e)


def delete_task(tasks):

    view_task(tasks)

    try:

        task_number = int(
            input(
                "\nEnter task number to delete: "
            ).strip()
        )

        if 1 <= task_number <= len(tasks["tasks"]):

            removed_task = tasks["tasks"].pop(
                task_number - 1
            )

            save_task(tasks)

            print(
                f"Deleted: "
                f"{removed_task['description']}"
            )

        else:

            print("Invalid task number.")

    except Exception as e:

        print(e)


def edit_task(tasks):

    view_task(tasks)

    try:

        task_number = int(
            input(
                "\nEnter task number to edit: "
            ).strip()
        )

        if 1 <= task_number <= len(tasks["tasks"]):

            task = tasks["tasks"][task_number - 1]

            new_description = input(
                "Enter new description: "
            ).strip()

            new_priority = input(
                "Enter new priority: "
            ).strip().lower()

            new_due_date = input(
                "Enter new due date: "
            ).strip()

            task["description"] = new_description
            task["priority"] = new_priority
            task["due_date"] = new_due_date

            save_task(tasks)

            print("Task updated.")

        else:

            print("Invalid task number.")

    except Exception as e:

        print(e)


def main():

    tasks = load_task()

    while True:

        print("\n===== TO-DO LIST MANAGER =====")

        print("1. View Task")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            view_task(tasks)

        elif choice == "2":

            create_task(tasks)

        elif choice == "3":

            marks_as_completed(tasks)

        elif choice == "4":

            delete_task(tasks)

        elif choice == "5":

            edit_task(tasks)

        elif choice == "6":

            print("\nGoodbye!")

            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":

    main()