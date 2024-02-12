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

if __name__ == "__main__":
    console = Console()
    if len(sys.argv) == 1:
        console.run_interactive()
    else:
        command = sys.stdin.readline().strip()
        console.run_non_interactive(command)
