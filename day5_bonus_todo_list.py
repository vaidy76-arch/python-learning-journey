import json
print("=== Todo List Manager ===")
print()

# Store tasks as list of dictionaries
# Each task: {"task": "Buy groceries", "completed": False}
tasks = []

while True:
    print("\n--- Menu ---")
    print("1. Add task")
    print("2. View all tasks")
    print("3. Mark task complete")
    print("4. Delete task")
    print("5. Show statistics")
    print("6. Exit")
    print("7. Edit Task")
    print("8. Save tasks to file")     
    print("9. Load tasks from file")

    choice = input("\nChoose option (1-9): ")
    
    if choice == "1":
        # Add task
        task_name=input("Enter Task: ")
        tasks.append({"task": task_name,"completed":False})
        print(f"{task_name} added ✅")
        
        
    elif choice == "2":
        # View all tasks
        if len(tasks)==0:
            print(f"Todo List is empty")
        else:
            for index,task in enumerate(tasks,1):
                status= "✅" if task["completed"] else "⬜"
                print(f"{index}.{status} {task['task']}")
        
        
    elif choice == "3":
        # Mark complete
        if len(tasks)==0:
            print(f"Todo List is empty")
        else:
            print("List of pending Tasks")
            for index,task in enumerate(tasks,1):
                status= "✅" if task["completed"] else "⬜"
                print(f"{index}.{status} {task['task']}")
            task_num=int(input("Enter task number to mark as complete:"))
            if task_num < 1 or task_num > len(tasks):
                print("❌ Invalid task number!")
            elif tasks[task_num-1]["completed"]:
                print("Task Already completed ✅")
            else:
                tasks[task_num -1]["completed"] = True
                print(f"{tasks[task_num -1]['task']} ✅ Marked complete!")
        
        
    elif choice == "4":
        # Delete task
        if len(tasks) == 0:
            print("❌ Todo List is empty")
        else:
        # Show tasks first
            for index, task in enumerate(tasks, 1):
                status = "✅" if task["completed"] else "⬜"
                print(f"{index}. {status} {task['task']}")
        
            task_num = int(input("Enter task number to delete: "))
        
            if task_num < 1 or task_num > len(tasks):
                print("❌ Invalid task number!")
            else:
                deleted = tasks.pop(task_num - 1)
                print(f"❌ Deleted: {deleted['task']}")
        
    elif choice == "5":
        # Show statistics
        total = len(tasks)
        completed = sum(1 for task in tasks if task["completed"])  # Count completed
        pending = total - completed

        print(f"Total tasks: {total}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")
        
        
    elif choice == "6":
        print("Goodbye! 👋")
        break

    elif choice =="7":

        if len(tasks)==0:
            print(f"Todo List is empty")
        else:
            
            for index,task in enumerate(tasks,1):
                status= "✅" if task["completed"] else "⬜"
                print(f"{index}.{status} {task['task']}")
            edit_task=int(input("Select which task to edit:"))

            if edit_task < 1 or edit_task > len(tasks):
                print("❌ Invalid task number!")
            else:
                old_name = tasks[edit_task - 1]["task"]
                print(f"Current task: {old_name}")
                new_task = input("Enter the New Task Name:")
                tasks[edit_task-1]["task"]=new_task
                print(f"✏️ Updated: '{old_name}' → '{new_task}'")
    elif choice=="8":
        try:
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=2)  # indent=2 makes it readable
            print(f"💾 Saved {len(tasks)} tasks to tasks.json")
        except Exception as e:
            print(f"❌ Error saving: {e}")
    
    elif choice == "9":
    # Load tasks from file
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
            print(f"📂 Loaded {len(tasks)} tasks from tasks.json")
        except FileNotFoundError:
            print("❌ No saved file found. Save some tasks first!")
        except json.JSONDecodeError:
            print("❌ File is corrupted - cannot load")
        except PermissionError:
            print("❌ No permission to read file")
        except Exception as e:
            print(f"❌ Error loading: {type(e).__name__} - {e}")
    else:
        print("❌ Invalid choice!")