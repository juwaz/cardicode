#!/usr/bin/env python3


class Node:
    def __init__(self, name, is_directory=False, parent=None):
        self.name = name
        self.is_directory = is_directory
        self.parent = parent
        self.children = None
        self.next_sibling = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, node):
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next_sibling:
                current = current.next_sibling
            current.next_sibling = node

    def find(self, name):
        current = self.head
        while current:
            if current.name == name:
                return current
            current = current.next_sibling
        return None

    def list_names(self):
        names = []
        current = self.head
        while current:
            names.append(current.name)
            current = current.next_sibling
        return names


class FileSystem:
    def __init__(self):
        self.root = Node("/", True)
        self.current_directory = self.root

    def ls(self):
        """
        List all files and directories in the current directory using the cursor.

        >>> fs = FileSystem()
        >>> fs.run_command('ls')
        []
        >>> fs.run_command('mkdir test')
        >>> fs.run_command('ls')
        ['test']
        >>> fs.run_command('touch file.txt')
        >>> fs.run_command('ls')
        ['test', 'file.txt']
        """
        if self.current_directory.children:
            return self.current_directory.children.list_names()
        return []

    def mkdir(self, name):
        """
        Create a directory with the specified name in the current directory using the cursor.

        >>> fs = FileSystem()
        >>> fs.run_command('mkdir mydir')
        >>> fs.run_command('ls')
        ['mydir']
        """
        if not self.current_directory.children:
            self.current_directory.children = LinkedList()
        if not self.current_directory.children.find(name):
            self.current_directory.children.add(
                Node(name, True, parent=self.current_directory)
            )

    def cd(self, directory_name):
        """
        Change the current directory to the specified directory or print error.

        >>> fs = FileSystem()
        >>> fs.mkdir('mydir')
        >>> fs.run_command('cd mydir')
        >>> fs.run_command('pwd')
        /mydir
        >>> fs.run_command('mkdir subdir')
        >>> fs.run_command('cd subdir')
        >>> fs.run_command('pwd')
        /mydir/subdir
        >>> fs.run_command('cd ..')
        >>> fs.run_command('cd ..')
        >>> fs.run_command('pwd')
        /
        >>> fs.run_command('cd non_existing_dir')
        cd: no such file or directory: "non_existing_dir"
        >>> fs.run_command('touch exists_but_not_dir.txt')
        >>> fs.run_command('cd exists_but_not_dir.txt')
        cd: not a directory: "exists_but_not_dir.txt"
        """

        if directory_name == "..":
            if self.current_directory.parent:
                self.current_directory = self.current_directory.parent
        else:
            dir_node = (
                self.current_directory.children.find(directory_name)
                if self.current_directory.children
                else None
            )
            if not dir_node:
                return f'cd: no such file or directory: "{directory_name}"'
            elif not dir_node.is_directory:
                return f'cd: not a directory: "{directory_name}"'

            self.current_directory = dir_node

    def touch(self, file_name):
        """
        Create a file with the specified name in the current directory.

        >>> fs = FileSystem()
        >>> fs.run_command('touch file.txt')
        >>> fs.run_command('ls')
        ['file.txt']
        """
        if not self.current_directory.children:
            self.current_directory.children = LinkedList()
        if not self.current_directory.children.find(file_name):
            self.current_directory.children.add(
                Node(file_name, False, parent=self.current_directory)
            )

    def print_cwd(self):
        path = []
        current = self.current_directory
        while current:
            path.append(current.name)
            current = current.parent
        path.pop()  # remove the empty string
        if path:
            pretty_path = "".join(f"/{path}" for path in reversed(path))
            print(pretty_path)
        else:
            print("/")

    def run_command(self, command_input):
        parts = command_input.strip().split(" ")
        command = parts[0]
        arg = parts[1] if len(parts) > 1 else None

        if command == "ls":
            print(self.ls())
        elif command == "mkdir" and arg:
            self.mkdir(arg)
        elif command == "cd" and arg:
            response = self.cd(arg)
            if response:
                print(response)
        elif command == "touch" and arg:
            self.touch(arg)
        elif command == "pwd":
            self.print_cwd()
        else:
            print(f"Command '{command}' not recognized or missing arguments.")


def main():
    fs = FileSystem()
    fs.print_cwd()

    while True:
        try:
            command_input = input("> ")
            fs.run_command(command_input)
        except KeyboardInterrupt:
            print("\nExiting.")
            break


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
