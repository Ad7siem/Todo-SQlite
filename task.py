import sqlite3

def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text)""")
    except:
        pass

def show_tasks(connection):
    cur = connection.cursor()
    cur.execute('''SELECT rowid, task FROM task''')
    result = cur.fetchall()

    for row in result:
        print(row[0], '-', row[1])

    print()


def add_tesk(connection):   
    print('Dodajemy zadanie.\n')
    task = input('Wpisz treść zadania: ')
    if task == '0':
        print('Powrót do menu')
    else:
        cur = connection.cursor()
        cur.execute('''INSERT INTO task(task) VALUES(?)''', (task,))
        connection.commit()
        print('Dodano zadanie\n')


def delete_task(connection):
    task_index = int(input("Podaj indeks zadania do usunięcia: "))
    cur = connection.cursor()
    rows_deleted = cur.execute('''DELETE FROM task WHERE rowid=?''', (task_index,)).rowcount
    connection.commit()

    if rows_deleted == 0:
        print('Takie zadanie nie istnieje')
    else:
        print('Usunięto zadanie!\n')

