class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task removed: {removed_task['task']}")
        else:
            print("Invalid task index.")

    def modify_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["task"] = new_task
            print(f"Task modified: {new_task}")
        else:
            print("Invalid task index.")

    def toggle_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            # Bug: Incorrectly toggling the completion status
            self.tasks[task_index]["completed"] = self.tasks[task_index]["completed"]
            status = "completed" if self.tasks[task_index]["completed"] else "not completed"
            print(f"Task marked as {status}: {self.tasks[task_index]['task']}")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Task list:")
            for index, task in enumerate(self.tasks):
                status = "[x]" if task["completed"] else "[ ]"
                print(f"{index}: {status} {task['task']}")

def main():
    todo_list = TodoList()

    while True:
        todo_list.display_tasks()
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Modify a task")
        print("4. Toggle task completion")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the new task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter the index of the task to remove: "))
            todo_list.remove_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter the index of the task to modify: "))
            new_task = input("Enter the new task: ")
            todo_list.modify_task(task_index, new_task)
        elif choice == '4':
            task_index = int(input("Enter the index of the task to toggle completion: "))
            todo_list.toggle_task(task_index)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()