class Max_heap:
    "Heap data structure which uses the binary tree property"
    def __init__(self, array) -> None:
        self.heap = array


    def left_node(self):
        for i in range(len(self.heap)-1):
            print(self.heap[2*i])

        

    def display(self):
        print(self.heap)


if __name__ == "__main__":
    array = [40, 50 , 60, 80, 90, 20, 21]

    mh = Max_heap(array)
    mh.left_node()