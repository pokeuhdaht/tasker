import json
import sys
import argparse




parser = argparse.ArgumentParser(
    prog='Tasker',
    description='Manage your LIFE!'
)

parser.add_argument('add', help='add help')

parser.add_argument('delete', help='delete help')

parser.add_argument('update', help='update help')

parser.parse_args(['add help'])