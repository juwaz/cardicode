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
        List all files and directories in the current directory.

        >>> fs = FileSystem()
        >>> fs.ls()
        []
        >>> fs.mkdir('test')
        >>> 'test' in fs.ls()
        True
        >>> fs.touch('file.txt')
        >>> 'file.txt' in fs.ls()
        True
        """
        if self.current_directory.children:
            return self.current_directory.children.list_names()
        return []

    def mkdir(self, name):
        """
        Create a directory with the specified name in the current directory.

        >>> fs = FileSystem()
        >>> fs.mkdir('mydir')
        >>> fs.ls()
        ['mydir']
        >>> fs.current_directory.children.head.is_directory
        True
        """
        if not self.current_directory.children:
            self.current_directory.children = LinkedList()
        if not self.current_directory.children.find(name):
            self.current_directory.children.add(
                Node(name, True, parent=self.current_directory)
            )

    def cd(self, directory_name):
        """
        Change the current directory to the specified directory.

        >>> fs = FileSystem()
        >>> fs.mkdir('mydir')
        >>> fs.cd('mydir')
        >>> fs.current_directory.name
        'mydir'
        >>> fs.cd('..')
        >>> fs.current_directory.name
        '/'
        >>> fs.cd('..')  # Should not move above root
        >>> fs.current_directory.name
        '/'
        """
        if directory_name == "..":
            if self.current_directory.parent:  # Prevent going above root
                self.current_directory = self.current_directory.parent
        else:
            dir_node = (
                self.current_directory.children.find(directory_name)
                if self.current_directory.children
                else None
            )
            if dir_node and dir_node.is_directory:
                self.current_directory = dir_node

    def touch(self, file_name):
        """
        Create a file with the specified name in the current directory.

        >>> fs = FileSystem()
        >>> fs.touch('file.txt')
        >>> fs.ls()
        ['file.txt']
        >>>
        >>>
        """
        if not self.current_directory.children:
            self.current_directory.children = LinkedList()
        if not self.current_directory.children.find(file_name):
            self.current_directory.children.add(
                Node(file_name, False, parent=self.current_directory)
            )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
