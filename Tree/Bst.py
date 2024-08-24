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

    def remove(self,data):
        if not self.root:
            print("Tree is empty!")
            return

        if self.root.data == data:
            self.root = None
            return

        self.recursiveRemove(self.root,data)

    def recursiveRemove(self,node,data):

        if node.left and node.left.data == data:
            node.left = None
            return

        if node.right and node.right.data == data:
            node.right = None
            return

        if data < node.data:
            self.recursiveRemove(node.left,data)
        else:
            self.recursiveRemove(node.right,data)

    def search(self,data):
        if not self.root:
            print("Tree is empty!")
            return
        if self.root.data == data:
            return True

        if self.recursiveSearch(self.root,data):
            return True
        return False


    def recursiveSearch(self,node,data):
        if node.left and node.left.data == data:
            return True

        if node.right and node.right.data == data:
            return True

        if data < node.data:
            return self.recursiveSearch(node.left,data)
        else:
            return self.recursiveSearch(node.right,data)



if __name__ == "__main__":


    bst = Bst()

    bst.add(40)
    bst.add(10)
    bst.add(50)
    bst.add(9)
    bst.add(15)
    bst.add(45)
    bst.add(60)


    bst.inorderDisplay()
    bst.preOrderDisplay()
    bst.postOrderDisplay()

    print(bst.search(1))
