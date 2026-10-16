import json
import sqlite3
import sys
import argparse

con = sqlite3.connect("tasker.db")
cursor = con.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT DEFAULT 'todo')
''')

def add_task(task:str) -> None: 
    cursor.execute("INSERT INTO tasks (name) VALUES (?)",(task,))
    #cursor.execute("SELECT * FROM tasks")
    con.commit()
    con.close()

def update_task(id:int,task:str) -> None:
    cursor.execute("UPDATE tasks SET name = ? WHERE id = ?",(task,id,))
    con.close();

def delete_task(id:int) -> None:
    cursor.execute("DELETE FROM tasks WHERE id = ?",(id,))
    con.commit()
    con.close()

def list_tasks() -> None:
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    print(rows)
    con.close()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Tasker - Simple Task Managing App')

    sub_parser = parser.add_subparsers(dest='command')
    
    add_parser = sub_parser.add_parser('add', help='Create a new task')
    add_parser.add_argument('task', type=str, help='Task being added')

    delete_parser = sub_parser.add_parser('delete', help='Delete an existing task')
    delete_parser.add_argument('id', type=int, help='ID of the task being deleted')

    update_parser = sub_parser.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='ID of the task being changed')
    update_parser.add_argument('task', help='The new name of the task')
    
    mark_in_progress_parser = sub_parser.add_parser('mark-in-progress', help='Mark task as "in-progress"')
    mark_in_progress_parser.add_argument('id', type=int, help='ID of the task being marked as "in-progress"')

    mark_done_parser = sub_parser.add_parser('mark-done', help='Mark task as Done')
    mark_done_parser.add_argument('id', type=int, help='ID of the task being marked as "done"')

    list_parser = sub_parser.add_parser('list', help="List all tasks")


    list_sub_parser = list_parser.add_subparsers(dest='list_command')
    
    list_todo_parser = list_sub_parser.add_parser('todo', help='List the remaing tasks that are marked as "to-do"')
    list_done_parser = list_sub_parser.add_parser('done', help='List the completed tasks that are marked as "done"')
    list_inprogress_parser = list_sub_parser.add_parser('in-progress', help='List the remaining tasks that are marked as "in-progress"')
    

    args = parser.parse_args()

    if args.command == 'add':
        print(f"add command: task: {args.task}")
        add_task(args.task)
    elif args.command == 'update':
        print(f"update command: id: {args.id} task: {args.task}")
        update_task(args.task,args.id)
    elif args.command == 'delete':
        print(f"delete command: id: {args.id}")
        delete_task(args.id)
    elif args.command == 'mark-done':
        print(f"mark-done command: id: {args.id}")
    elif args.command == 'mark-in-progress':
        print(f"mark-in-progress command: id: {args.id}")
    elif args.list_command == 'todo':
        print(f"todo command")
    elif args.list_command == 'done':
        print(f"done command")
    elif args.list_command == 'in-progress':
        print(f"in-progress command")
    elif args.command == 'list':
        print(f"list command")
        list_tasks()
    else:
        print(f"Something went wrong")
