class Node:
    def __init__(self,data):
        self.element = data
        self.pointer = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.temp = None


    def add_element(self,data):
        if self.head is None:
            new_node = Node(data)
            self.temp = new_node
            self.head = new_node
            self.head.pointer = self.head
        else:
            cur = self.head
            if cur.pointer == cur:
                new_node = Node(data)
                new_node.pointer = self.head
                cur.pointer = new_node
            else:
                cur = self.head
                new_node = Node(data)
                while cur.pointer != self.head:
                    cur = cur.pointer

                new_node.pointer = self.head
                cur.pointer = new_node


    def traverse(self,stop_at_element):
        cur = self.head

        while cur.element != stop_at_element:
            print(cur.element)
            cur = cur.pointer




cll = CircularLinkedList()
cll.add_element(10)
cll.add_element(20)
cll.add_element(30)
cll.add_element(40)
cll.add_element(50)
cll.add_element(60)
cll.add_element(70)
cll.add_element(80)

cll.traverse(60)
