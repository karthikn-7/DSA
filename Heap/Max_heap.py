class Max_heap:
    "Heap data structure which uses the binary tree property"
    def __init__(self, array) -> None:
        self.heap = array


    def left_node(self):
        "Prints all the left node"
        for i in range(len(self.heap)):
            ln = (2 * i) + 1
            if ln > len(self.heap)-1:
                break
            print(self.heap[ln])
    
    def right_node(self):
        "Prints all the right node."
        for i in range(len(self.heap)):
            ln = (2 * i) + 2
            if ln > len(self.heap)-1:
                break
            print(self.heap[ln])
        
    def parent_node(self, child):
        "Returns the parent node for the given child,else return -1"
        if type(child) is str or type(child) is bool or type(child) is float:
            return -1

        if child > len(self.heap):
            return -1
        
        return (child - 1) // 2

    def display(self):
        print(self.heap)


if __name__ == "__main__":
    array = [20, 21, 12, 31, 42, 50, 11]

    mh = Max_heap(array)
    print(mh.parent_node(1.2))

    