import json
import sqlite3
import argparse

con = sqlite3.connect("tasker.db")
cursor = con.cursor()
# creates a new DB file if one does not already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT DEFAULT 'to do',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT NULL)
''')

# adds a task to the db file
def add_task(task:str) -> None: 
    cursor.execute("INSERT INTO tasks (name) VALUES (?)",(task,))
    con.commit()
    con.close()

# update a task
def update_task(task:str,id:int) -> None:
    cursor.execute("UPDATE tasks SET name = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",(task,id))
    con.commit()
    con.close()

# delete a task
def delete_task(id:int) -> None:
    cursor.execute("DELETE FROM tasks WHERE id = ?",(id,))
    con.commit()
    con.close()

# list a task
def list_tasks() -> None:
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    con.close()
    for row in rows:
        print(f"ID: {row[0]:<3} | {row[1]:^27} | Status: {row[2]} | Created at: {row[3]} | Updated at: {row[4]}")

# list tasks marked as 'to do'
def list_todo_tasks() -> None:
    cursor.execute("SELECT * FROM tasks WHERE status = 'to do'")
    rows = cursor.fetchall()
    con.close()
    if not rows:
        print(f"No tasks markes as 'to do'")
    else:
        for row in rows:
            print(f"ID: {row[0]:<3} | {row[1]:^27} | Status: {row[2]} | Created at: {row[3]} | Updated at: {row[4]}")

# list tasks marked as 'done'
def list_done_tasks() -> None:
    cursor.execute("SELECT * FROM tasks WHERE status = 'done'")
    rows = cursor.fetchall()
    con.close()
    if not rows:
        print(f"No tasks markes as 'done'")
    else:
        for row in rows:
            print(f"ID: {row[0]:<3} | {row[1]:^27} | Status: {row[2]} | Created at: {row[3]} | Updated at: {row[4]}")

# list tasks marked as 'in-progress'
def list_in_progress_tasks() -> None:
    cursor.execute("SELECT * FROM tasks WHERE status = 'in-progress'")
    rows = cursor.fetchall()
    con.close()
    if not rows:
        print(f"No tasks markes as 'in-progress'")
    else:
        for row in rows:
            print(f"ID: {row[0]:<3} | {row[1]:^27} | Status: {row[2]} | Created at: {row[3]} | Updated at: {row[4]}")

# mark task as 'to do'
def mark_task_todo(id:int) -> None:
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?",("to do", id))
    con.commit()
    con.close()

# mark task as 'in-progress'
def mark_task_in_progress(id:int) -> None:
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?",("in-progress", id))
    con.commit()
    con.close()

# mark task as 'done'
def mark_task_done(id:int) -> None:
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?",("done",id))
    on.commit()
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
    
    mark_todo_parser = sub_parser.add_parser('mark-todo', help='Mark task as To Do')
    mark_todo_parser.add_argument('id', type=int, help='ID of the task being marked as "to do"')

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

    if args.command == 'add':                                       # Add task
        add_task(args.task)
        print(f"Added '{args.task}' to list.")
    elif args.command == 'update':                                  # Update task
        update_task(args.task,args.id)
        print(f"Updated task id: {args.id} to be named '{args.task}'")
    elif args.command == 'delete':                                  # Delete task
        delete_task(args.id)
        print(f"Deleted task with id: {args.id}")
    elif args.command == 'mark-todo':                               # Mark task as 'to do'
        mark_task_todo(args.id)
        print(f"marked task id {args.id} as: 'to do'")
    elif args.command == 'mark-done':                               # Mark task as 'done'
        mark_task_done(args.id)
        print(f"marked task id {args.id} as: 'done'")
    elif args.command == 'mark-in-progress':                        # Mark task as 'in-progress'
        mark_task_in_progress(args.id)
        print(f"marked task id {args.id} as: 'in-progress'")
    elif args.list_command == 'todo':                               # List all tasks marked 'to do'
        list_todo_tasks()
    elif args.list_command == 'done':                               # List all tasks marked as 'done'
        list_done_tasks()
    elif args.list_command == 'in-progress':                        # List all tasks marked as 'in-progress'abs
        list_in_progress_tasks()
    elif args.command == 'list':                                    # List all tasks
        list_tasks()
    else:                                                           
        print(f"Something went wrong")