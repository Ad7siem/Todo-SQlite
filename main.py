from task import create_table, show_tasks, add_tesk, delete_task
import sqlite3

connection = sqlite3.connect('todo.db')
create_table(connection)

while True:
    print('1. Pokaż zadania')
    print('2. Dodaj zadanie')
    print('3. Usuń zadanie')
    print('4. Wyjdź')

    try:
        user_choice = int(input('Wybierz liczbę: '))
    except:
        print("Nie podano wartości id zadania.\n")
        continue
    print()

    if user_choice == 1:
        show_tasks(connection)

    if user_choice == 2:
        add_tesk(connection)

    if user_choice == 3:
        delete_task(connection)

    if user_choice == 4:
        break

connection.close()


