import json
import sys
import argparse




def main() -> None:
    parser = argparse.ArgumentParser(description='Tasker - Simple Task Managing App')

    sub_parser = parser.add_subparsers(dest='argument')
    
    add_parser = sub_parser.add_parser('add', help='Add a task to the list')
    add_parser.add_argument('task', type=str, help='Task being added')

    update_parser = sub_parser.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='ID for the task being changed')
    update_parser.add_argument('task', help='The new name of the task')
    



























if __name__ == "__main__":
    main()