from tasks import add_task, list_tasks, complete_task, delete_task
from storage import load_tasks, save_tasks

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Dodaj zadanie")
        print("2. Pokaż zadania")
        print("3. Oznacz jako wykonane")
        print("4. Usuń zadanie")
        print("5. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            title = input("Treść zadania: ")
            tasks = add_task(tasks, title)

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            index = int(input("Numer zadania: "))
            tasks = complete_task(tasks, index)

        elif choice == "4":
            index = int(input("Numer zadania: "))
            tasks = delete_task(tasks, index)

        elif choice == "5":
            save_tasks(tasks)
            break

        else:
            print("Nieprawidłowa opcja!")

if __name__ == "__main__":
    main()