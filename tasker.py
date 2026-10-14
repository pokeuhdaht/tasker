import json
import sys
import argparse




parser = argparse.ArgumentParser(
    prog='Tasker',
    description='Manage your LIFE!'
)




#parser.add_argument()





subparsers = parser.add_subparsers()

parser_add = subparsers.add_parser('add', help='add help')

parser_delete = subparsers.add_parser('delete', help='delete help')

parser_update = subparsers.add_parser('update', help='update help')


parser.parse_args(['add', '-h'])
