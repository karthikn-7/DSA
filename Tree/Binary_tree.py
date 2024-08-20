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

bt = BinaryTree()
bt.add(10)
bt.add(20)
bt.add(30)
bt.add(40)
bt.add(50)
bt.add(60)
bt.add(70)

bt.display()