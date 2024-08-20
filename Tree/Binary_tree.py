class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self,data):
        if not self.root:
            node = Node(data)
            self.root = node
            return
        self.recursiveAdd(data,self.root)

    def recursiveAdd(self,data,node):
        if not node.left:
            node.left = Node(data)
        elif not node.right:
            node.right = Node(data)
        else:
            self.recursiveAdd(data,node.left)

    def display(self,depth=0,node=None):
        if not node:
            node = self.root
        
        print(" "*depth,node.data)

        if node.left:
            self.display(depth+1,node.left)
        if node.right:
            self.display(depth+1,node.right)

    def remove(self,data):
        if not self.root:
            print("Binary tree is empty!")
            return
        if self.root.data == data:
            self.root = None
            return
        self.removeRecursive(data,self.root)
        
        
    def removeRecursive(self,data,node):
        if node.left:
            if node.left.data == data:
                node.left = None
                return
        if node.right:
            if node.right.data == data:
                node.right = None
                return
        if node.left:
            self.removeRecursive(data,node.left)

    def search(self,data):
        if self.root.data == data:
            return True
        
        return self.recursiveSearch(data,self.root)
        
        
    def recursiveSearch(self,data,node):
        if node and node.data == data:
            return True
        if node:
            return self.recursiveSearch(data,node.left) or self.recursiveSearch(data,node.right)
        return False
        
        

bt = BinaryTree()
bt.add(10)
bt.add(20)
bt.add(30)
bt.add(40)
bt.add(50)
bt.add(60)
bt.add(70)
bt.display()
