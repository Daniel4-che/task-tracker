
import json 
from os import path
from datetime import datetime
from handlers.parsers import arg_parsers
taskfile="taskes.json"
class Taskes:
    def __init__(self, taskfile):
        self.taskfile=taskfile
        self.items=self.load_taskes()
    
    def load_taskes(self):
        if path.exists(self.taskfile):
            with open(self.taskfile, "r") as file:
                return json.load(file)
        return [] 
    
    def save_taskes(self):
        with open(self.taskfile,"w" )as file:
            json.dump(self.items, file, indent=4)

    def add_task(self, description):
        timestamp=datetime.now().isoformat()
        self.items.append({
            "id": len(self.items) + 1,
            "description":description,
            "status":"todo",
            "createdAt": timestamp,
            "updatedAt": timestamp,
        })
        self.save_taskes()
    
    def update_task():
        pass

    def delete_task():
        pass

    def list_tasks():
        pass

    def mark_task():
        pass


def main():
    args=arg_parsers()
    taskes=Taskes(taskfile)
    if args.command=="add" and args.description:
        taskes.add_task(args.description)
main()