#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node: # create a node with boolean value
    def __init__(self, name:str, isFile:bool):
        self.name = name
        self.isFile = isFile
        self.children = []
        
    def add_child(self, child): # add child node to list of children for tree structure
        self.children.append(child)
        
    def __repr__(self):
        return self.name
        
class FileSystem:
    def __init__(self):
        self.root = Node("root", False)
        self.current = self.root  # sets current directory to root
        
    def mkdir(self, name:str):
        new_dir = Node(name, False)
        self.current.add_child(new_dir)
        print(f"Directory {name} created.")
    
    def touch(self, name:str):
        new_file = Node(name, True)
        self.current.add_child(new_file)
        print(f"File {name} created.")
    
    def cd(self, name:str):
        for child in self.current.children: # navigate through directory with loop
            if child.name == name:
                if not child.isFile:
                    self.current = child
                    print(f"Changed to directory {name}.")
                    return
                else:
                    print(f"{name} is a file.")
                    return
        print(f"{name} not found.")
    
    def ls(self):
        for child in self.current.children:
            print(child)
    
    def pwd(self):
        path = []
        node = self.current
        while node.name != "root":
            path.append(node.name)
            node = node.parent
        print("/".join(path[::-1]))
    
fs = FileSystem()
while True:
    command = input("Enter command (mkdir, touch, cd, ls, pwd, exit): ")
    if command == "mkdir":
        name = input("Enter directory name: ")
        fs.mkdir(name)
    elif command == "touch":
        name = input("Enter file name: ")
        fs.touch(name)
    elif command == "cd":
        name = input("Enter directory name: ")
        fs.cd(name)
    elif command == "ls":
        fs.ls()
    elif command == "pwd":
        fs.pwd()
    elif command == "exit":
        break
    else:
        print("Invalid command.")


# In[ ]:





# In[ ]:




