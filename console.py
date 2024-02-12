#!/usr/bin/python3
"""
console.py - Interactive command-line interface
"""

import sys


class Console:
    """
    Class documentation: This class represents the interactive console.
    """

    def __init__(self):
        """
        Function documentation: Initialize the console.
        """
        self.commands = {
            'help': self.help,
            'quit': self.quit
        }

    def help(self):
        """
        Function documentation: Display help information.
        """
        print("Documented commands (type help <topic>):")
        print("=" * 40)
        print("EOF  help  quit")

    def quit(self):
        """
        Function documentation: Exit the console.
        """
        sys.exit()

    def run_interactive(self):
        """
        Function documentation: Run the console in interactive mode.
        """
        print("(hbnb)")
        while True:
            try:
                command = input().strip()
                if command in self.commands:
                    self.commands[command]()
                else:
                    print(f"Invalid command: {command}")
            except EOFError:
                print()
                sys.exit()

    def run_non_interactive(self, command):
        """
        Function documentation: Run the console in non-interactive mode.
        """
        if command in self.commands:
            self.commands[command]()
        else:
            print(f"Invalid command: {command}")

def default(self, line):
        """Method to take care of following commands:
        <class name>.all()
        <class name>.count()
        <class name>.show(<id>)
        <class name>.destroy(<id>)
        <class name>.update(<id>, <attribute name>, <attribute value>)
        <class name>.update(<id>, <dictionary representation)

        Description:
            Creates a list representations of functional models
            Then use the functional methods to implement user
            commands, by validating all the input commands

        """
        names = ["BaseModel", "User", "State", "City", "Amenity",
                 "Place", "Review"]

        commands = {"all": self.do_all,
                    "count": self.my_count,
                    "show": self.do_show,
                    "destroy": self.do_destroy,
                    "update": self.do_update}

        args = re.match(r"^(\w+)\.(\w+)\((.*)\)", line)
        if args:
            args = args.groups()
        if not args or len(args) < 2 or args[0] not in names \
                or args[1] not in commands.keys():
            super().default(line)
        return

        if args[1] in ["all", "count"]:
            commands[args[1]](args[0])
        elif args[1] in ["show", "destroy"]:
            commands[args[1]](args[0] + ' ' + args[2])
        elif args[1] == "update":
            params = re.match(r"\"(.+?)\", (.+)", args[2])
            if params.groups()[1][0] == '{':
                dic_p = eval(params.groups()[1])
                for k, v in dic_p.items():
                    commands[args[1]](args[0] + " " + params.groups()[0] +
                                      " " + k + " " + str(v))
            else:
                rest = params.groups()[1].split(", ")
                commands[args[1]](args[0] + " " + params.groups()[0] + " " +
                                  rest[0] + " " + rest[1])


if __name__ == '__main__':
    cli = HBNBCommand()
    cli.cmdloop()

