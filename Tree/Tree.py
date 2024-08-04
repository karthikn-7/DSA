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
        
    

if __name__ == "__main__":
        
    Tr = Tree()
    Tr.add(10)
    Tr.add(20,10)
    Tr.add(30,10)
    Tr.add(40,10)
    Tr.add(50,40)

    for data in Tr.root.children:
        print(data.data)
