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
        if self.root:
            self._inorder(self.root)

    
    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            print(node.data,end=" ")
            self._inorder(node.right)

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

    def delete(self,data):
        if not self.root:
            print("Tree is empty!")
            return

        self._deleteRecursive(self.root,data)
        


    def _deleteRecursive(self,node,data):

        if node and data < node.data:
            if node.left.data == data and not node.left.left and not node.left.right:
                node.left = None
                return
            self._deleteRecursive(node.left,data)
        if node and data > node.data:
            if node.right.data == data and not node.right.left and not node.right.right:
                node.right = None
                return
            self._deleteRecursive(node.right,data)

        if node.data == data:
            if node.left and not node.right:
                node.data = node.left.data
                node.left = None
                return
            elif node.right and not node.left:
                node.data = node.right.data
                node.right = None
                return
            
            elif node.data < self.root.data:
                lastMax = self.inorderPredecessor(node)
                node.data = lastMax
                self.removeInorderPreNode(node)
                return

            
    def minValueNode(self):
        if not self.root:
            return None
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return cur.data
    
    def inorderPredecessor(self,node=None):
        cur = node
        while cur.right is not None:
            cur = cur.right

        if node:
            return cur.data


    def removeInorderPreNode(self,node):
        cur = node
        while cur.right.right is not None:
            cur = cur.right

        cur.right = None

    def inorderSuccessor(self,node=None):
        
        cur = node
        while cur.right is not None:
            cur = cur.right
            if cur.left:
                return self.inorderSuccessor(cur.left)
            
        if cur.left:
            return self.inorderSuccessor(cur.left)
        return cur.data




if __name__ == "__main__":


    bst = Bst()

    bst.add(40)
    bst.add(10)
    bst.add(50)
    bst.add(9)
    bst.add(15)
    bst.add(45)
    bst.add(60)
    bst.add(4)
    bst.add(9.5)
    bst.add(55)
    bst.add(56)
    bst.add(15)
    bst.add(11)
    bst.add(14)
    bst.add(16)
    bst.add(30)
    bst.add(25)

    bst.inorderDisplay()
    print()
    print(bst.inorderSuccessor(bst.root.left.right))
    bst.inorderDisplay()
    print()