import os
import json
import argparse
from datetime import datetime

if "todolist.json" in os.listdir():
    with open("todolist.json", "r") as f:
        todolist_dict = json.load(f)
else:
    todolist_dict = {}

def todo_id_generator(todo_list):
    count = 1
    while True:
        if str(count) not in todo_list:
            break
        else:
            count += 1
    return count

def add_todo(args):
    if todolist_dict == {}:
        todo_dict = {
            "id": 1,
            "description": args.description,
            "status": "todo",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        todolist_dict[todo_dict["id"]] = todo_dict
        with open("todolist.json", "w") as fp:
            json.dump(todolist_dict, fp, default=str)
        print(f"Task added succesfully (ID: {todo_dict['id']})")
    else:
        todo_ids = list(todolist_dict.keys())
        print(todo_ids)
        todo_id = todo_id_generator(todo_ids)
        print(todo_id)
        todo_dict = {
            "id": todo_id,
            "description": args.description,
            "status": "todo",
            "createdAt": datetime.now(),
            "updatedAt": datetime.now()
        }
        todolist_dict[todo_dict["id"]] = todo_dict
        with open("todolist.json", "w") as fp:
            json.dump(todolist_dict, fp, default=str)
        print(f"Task added succesfully (ID: {todo_dict['id']})")

def update_todo(args):
    if str(args.id) in todolist_dict.keys():
        todolist_dict[str(args.id)]['description'] = args.new_description
        with open("todolist.json", "w") as fp:
            json.dump(todolist_dict, fp, default=str)
    elif args.id not in todolist_dict.keys():
        print("A todo with that ID does not exist. Create a new todo with 'add'.")

def delete_todo(args):
    try:
        del todolist_dict[str(args.id)]
        with open("todolist.json", "w") as fp:
            json.dump(todolist_dict, fp, default=str)
    except KeyError:
        print("A todo with that ID does not exist. Create a new todo with 'add'.")

def in_progress_todo(args):
    try:
        todolist_dict[str(args.id)]["status"] = "in-progress"
        with open("todolist.json", "w") as fp:
            json.dump(todolist_dict, fp, default=str)
    except KeyError:
        print("A todo with that ID does not exist. Create a new todo with 'add'.")

def done_todo(args):
    try:
        todolist_dict[str(args.id)]["status"] = "done"
        with open("todolist.json", "w") as fp:
            json.dump(todolist_dict, fp, default=str)
    except KeyError:
        print("A todo with that ID does not exist. Create a new todo with 'add'.")

def list_todo(args):
    if args.filter == "all":
        descriptions = [value["description"] for value in todolist_dict.values()]
        print("All Tasks:")
        if len(descriptions) > 0:
            [print(description) for description in descriptions]
        else:
            print("You have no todos. Create a new todo with 'add'.")    
    elif args.filter == ["done"]:
        descriptions = [value["description"] for value in todolist_dict.values() if value["status"] == "done"]
        print("Completed Tasks:")
        if len(descriptions) > 0:
            [print(description) for description in descriptions]
        else:
            print("You have no completed todos. Create a new todo with 'add'.")   
    elif args.filter == ["todo"]:
        descriptions = [value["description"] for value in todolist_dict.values() if value["status"] == "todo"]
        print("Tasks To Do:")
        if len(descriptions) > 0:
            [print(description) for description in descriptions]
        else:
            print("You have no todos. Create a new todo with 'add'.")   
    else:
        descriptions = [value["description"] for value in todolist_dict.values() if value["status"] == "inprogress"]
        print("Tasks In Progress:")
        if len(descriptions) > 0:
            [print(description) for description in descriptions]
        else:
            print("You have no todos. Create a new todo with 'add'.")   

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(required=True)

parser_add = subparsers.add_parser("add")
parser_add.add_argument("description", type=str)
parser_add.set_defaults(func=add_todo)

parser_update = subparsers.add_parser("update")
parser_update.add_argument("id", type=int)
parser_update.add_argument("new_description", type=str)
parser_update.set_defaults(func=update_todo)

parser_delete = subparsers.add_parser("delete")
parser_delete.add_argument("id", type=int)
parser_delete.set_defaults(func=delete_todo)

parser_in_progress = subparsers.add_parser("mark-in-progress")
parser_in_progress.add_argument("id", type=int)
parser_in_progress.set_defaults(func=in_progress_todo)

parser_in_progress = subparsers.add_parser("mark-done")
parser_in_progress.add_argument("id", type=int)
parser_in_progress.set_defaults(func=done_todo)

parser_list = subparsers.add_parser("list")
parser_list.add_argument("filter", choices=["done", "todo", "inprogress", "all"], 
                         nargs="*", default="all")
parser_list.set_defaults(func=list_todo)

args = parser.parse_args()
args.func(args)
