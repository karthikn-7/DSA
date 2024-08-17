class Tree_node:
    def __init__(self,data) -> None:
        self.data = data
        self.children = []


class Tree:
    def __init__(self):
        self.root = None

    def add(self,data,parent_data = None):
        node = Tree_node(data)
        if self.root is None:
            self.root = node
            return 
        
        parent_node = self.find_parent_node(parent_data,self.root)
        if parent_node is None:
            raise Exception("Parent Not Found")
        parent_node.children.append(node)


    def find_parent_node(self,data,node):
        if node.data == data:
            return node
        
        
        for child in node.children:
            nodefound = self.find_parent_node(data,child)
            if nodefound is not None:
                return nodefound
        
        return None

    def display(self,depth=0,node = None):

        if not node:
            node = self.root
        
        if not node:
            print("Node is empty")
            return

        print(" "*depth, node.data)
        for child in node.children:
            self.display(depth=depth+1,node=child)

    def remove(self,data):
        if not self.root:
            print("Root is empty")
            return

        if data == self.root.data:
            self.root = None
            return
        
        parentNode = self.find_parent(data,self.root)
        if parentNode:
            for child in parentNode.children:
                if child.data == data:
                    parentNode.children.remove(child)
                    return
        print("node not found")


    
    def find_parent(self,data,node):
        for child in node.children:
            if child.data == data:
                return node
            nodefound = self.find_parent(data,child)
            if nodefound:
                return nodefound
        
        return None


if __name__ == "__main__":

    Tr = Tree()
    Tr.add(10)
    Tr.add(20,10)
    Tr.add(30,10)
    Tr.add(40,10)
    Tr.add(50,40)
    Tr.add(12,40)
    Tr.add(99,50)
    Tr.add(23,50)
    Tr.add(42,50)
    

    Tr.display()
    print("\n\n")
    Tr.remove(50)
    Tr.display()