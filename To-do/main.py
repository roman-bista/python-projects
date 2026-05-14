# load exitisig item
# create new item
# list item
# mark item as complete
# save item
import json

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_name = os.path.join(BASE_DIR, "todo_list.json")

def load_task():
    try:
        with open(file_name,"r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_task(tasks):
    try:
        with open(file_name,"w") as file:
            json.dump(tasks,file,indent=4)       #This converts Python data into JSON format and writes it to file.
    
    except Exception as e:
        print("Error:", e)
    
def view_task(tasks):
    print()
    task_list=tasks["tasks"]
    if len(task_list)==0:
        print("empty no task to display")
    else:
        print("Your To-do list: ")
        for idx,task in enumerate(task_list):
            status = "[completed]" if task["complete"] else "[pending]"
            print(f"{idx+1}. {task['description']}| {status}")


def create_task(tasks):
    description = input("Enter task description: ").strip()
    if description:
        tasks["tasks"].append( #task[tasks] ma chai add garnu
            {"description" : description, 
             "complete":False }
             )
        save_task(tasks)
        print("tasks added. ")
    else:
        print("Description cannot be empty.")

def marks_as_completed(tasks):
    view_task(tasks)
    try:
        task_number=int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_task(tasks)
            print("Task marked as complete.")
        else:
            print("invalid")
    except Exception as e:
        print(e)
def main():
    tasks=load_task()

    while True:
        print("\n To-Do List Manager")
        print("1. View Task")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice=input("Enter your choice: ").strip()
        if choice=="1":
            view_task(tasks)
        elif choice=="2":
            create_task(tasks)
        elif choice=="3":
            marks_as_completed(tasks)
        elif choice=="4":
            print("Good bye thanks for playing")
            break
        else:
            print("Invalid choice.please try again ")

if __name__ == "__main__":
    main()
# main()