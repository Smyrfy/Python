todo_list = []  # Створюємо порожній список для задач

def show_menu():
    print("\nОберіть дію:")
    print("1. Додати задачу")
    print("2. Показати задачі")
    print("3. Видалити задачу")
    print("4. Вийти")

def add_task():
    task = input("Введіть назву задачі: ")
    todo_list.append(task)  # Додаємо задачу до списку
    print("Задачу додано!")

def show_tasks():
    if not todo_list:
        print("Список порожній.")
    else:
        print("Ваші задачі:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")  # Нумеруємо задачі

def delete_task():
    show_tasks()
    try:
        index = int(input("Введіть номер задачі для видалення: "))
        if 1 <= index <= len(todo_list):
            removed = todo_list.pop(index - 1)  # Видаляємо задачу за індексом
            print(f"Задача '{removed}' видалена.")
        else:
            print("Невірний номер.")
    except ValueError:
        print("Потрібно ввести число!")

# Основний цикл програми
while True:
    show_menu()
    choice = input("Ваш вибір: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("До побачення!")
        break  # Вихід із циклу
    else:
        print("Невірний вибір, спробуйте ще раз.")


