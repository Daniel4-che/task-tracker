import argparse

def arg_parsers():
    parser=argparse.ArgumentParser(description="Daniel's task tracker CLI")
    subparsers=parser.add_subparsers(dest="command")

    #add subparser
    add_subparser=subparsers.add_parser("add", help="To add task use the add command")
    add_subparser.add_argument("description", help="Description is required", type=str)

    #Update subparser
    updatesubparser=subparsers.add_parser("update", help="To update task use the update command")
    updatesubparser.add_argument("id", help="id is required", type=int)
    updatesubparser.add_argument("description", help= "Description is required", type=str)

    deletesubparsers=subparsers.add_parser("delete", help="To delete a task you use the delete command")
    deletesubparsers.add_argument("id", help="id is required", type=int)
    deletesubparsers.add_argument("description", help="description is required", type=str)

    markinprogresssubparsers=subparsers.add_parser("mark-in-progress", help="To run this command use mark-in-progress")
    markinprogresssubparsers.add_argument("id", help="id is required", type=int)
    markdonesubparsers=subparsers.add_parser("mark-done", help="To run this command use mark-done")
    markdonesubparsers.add_argument("id", help="id is required", type=int)
    listparser=subparsers.add_parser("list", help="To list taskes use the list command")
    listparser.add_argument("status", nargs="?", choices=["done", "todo", "in-progress"], help="command to run - done, todo, in-progress", type=str)
    return parser.parse_args()