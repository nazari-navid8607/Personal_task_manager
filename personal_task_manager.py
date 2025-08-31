import sqlite3
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

def add_task():
    title = input("title of your task: ")
    duration = input("duration(mins): ")
    status = False
    cursor.execute("INSERT INTO tasks VALUES (?, ?, ?)", (title, f"{duration} mins", status))
    connection.commit()
    return True

def show_task():
    for task in cursor.execute("SELECT title, duration, status FROM tasks"):
        print(task)

def delete_task():
    title = input("Enter task name: ")
    existance = cursor.execute("SELECT EXISTS(SELECT 1 FROM tasks WHERE title = ?)",(title,)).fetchone()[0]
    if existance == 0:
        print(f"No task named {title}.")
    elif existance == 1:
        cursor.execute("DELETE FROM tasks WHERE title = ?", (title,))
        connection.commit()
        print("Task successfully deleted")

while True:
    action = input("command: ").lower().strip()
    if action in ["new task", "nt"]:
        stat = add_task()
        if stat == True:
            print("Task added successfully.")
    elif action == "show":
        show_task()
    elif action in ["del", "delete"]:
        delete_task()
    elif action in ["exit", "quit"]:
        connection.close()
        exit()
    elif action.lower().strip() == "help":
        print('You can add a task by command "new task" or "nt".')
        print('You can delete a task using "delete" or "del.')
        print('To print tasks, simply enter "show".')
        print('Enter "quit" or "exit" to save the tasks and quit.')
    else:
        print("Invalid operation")
        print('For more information, enter "help"')
    
