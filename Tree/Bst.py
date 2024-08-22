class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Bst:
    def __init__(self) -> None:
        self.root = None

    def add(self,data):
        newNode = Node(data)
        if not self.root:
            self.root = newNode
            return
        self.recursiveAdd(data,self.root)
        
    def recursiveAdd(self,data,node=None):

        if data < node.data:
            if not node.left:
                newNode = Node(data)
                node.left = newNode
                return
            else:
                self.recursiveAdd(data,node.left)
        elif data > node.data:
            if not node.right:
                newNode = Node(data)
                node.right = newNode
                return
            else:
                self.recursiveAdd(data,node.right)

    def inorderDisplay(self):
        result = []
        self.inorderTraversal(self.root,result)
        print(result)
    
    def preOrderDisplay(self):
        result = []
        self.preOrderTraversal(self.root,result)
        print(result)

    def postOrderDisplay(self):
        result = []
        self.postOrderTraversal(self.root,result)
        print(result)


    def inorderTraversal(self,node,result):
        if not node:
            return None
        else:
            self.inorderTraversal(node.left,result)
            result.append(node.data)
            self.inorderTraversal(node.right,result)

    def preOrderTraversal(self,node,result):
        if not node:
            return None
        else:
            result.append(node.data)
            self.inorderTraversal(node.left,result)
            self.inorderTraversal(node.right,result)

    def postOrderTraversal(self,node,result):
        if not node:
            return None
        else:
            self.inorderTraversal(node.left,result)
            self.inorderTraversal(node.right,result)
            result.append(node.data)

if __name__ == "__main__":


    bst = Bst()

    bst.add(45)
    bst.add(20)
    bst.add(10)
    bst.add(5)
    bst.add(6)
    bst.add(19)
    bst.add(21)
    bst.add(51)


    bst.inorderDisplay()
    bst.preOrderDisplay()
    bst.postOrderDisplay()