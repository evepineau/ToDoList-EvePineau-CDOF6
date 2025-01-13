class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tâche ajoutée: {task}")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Tâche supprimée: {removed_task}")
        else:
            print("Index de tâche invalide.")

    def modify_task(self, task_index, new_task):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index] = new_task
            print(f"Tâche modifiée: {new_task}")
        else:
            print("Index de tâche invalide.")

    def display_tasks(self):
        if not self.tasks:
            print("Aucune tâche dans la liste.")
        else:
            print("Liste des tâches:")
            for index, task in enumerate(self.tasks):
                print(f"{index}: {task}")

def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Ajouter une tâche")
        print("2. Supprimer une tâche")
        print("3. Modifier une tâche")
        print("4. Afficher les tâches")
        print("5. Quitter")

        choice = input("Choisissez une option: ")

        if choice == '1':
            task = input("Entrez la nouvelle tâche: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Entrez l'index de la tâche à supprimer: "))
            todo_list.remove_task(task_index)
        elif choice == '3':
            task_index = int(input("Entrez l'index de la tâche à modifier: "))
            new_task = input("Entrez la nouvelle tâche: ")
            todo_list.modify_task(task_index, new_task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()