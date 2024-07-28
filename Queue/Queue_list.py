class Node:
    """Node for the Implementing the list."""
    def __init__(self,data):
        self.element = data
        self.next = None
    

class Queue:
    """Queue - FIFO - First in First Out"""

    def __init__(self):
        self.head = None

    def enqueue(self,element:any) -> None:
        """Adds new elements in the queue"""
        if self.head is None:
            new_node = Node(element)
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            
            new_node = Node(element)
            cur.next = new_node
    
    def dequeue(self) -> None:
        """Removes the first element in the queue"""
        if self.head is None:
            raise Exception("Queue is empty,unable to delete.")
        elif self.head is not None:
            # if the head is not none it removes the first element
            new_head = self.head.next
            self.head.next = None
            self.head = new_head
        elif self.head.next is None:
            # if head is have only one element then it sets the head to none
            self.head = None
        
            

    def peek(self) -> any:
        """Returns the first element in the list"""
        if self.head is None:
            # if the head is none then returns -1
            return -1
        else:
            # else it returns the first element of the queue
            return self.head.element
    
    def is_empty(self) -> bool:
        """Returns boolean if the Queue is empty it returns false,else true"""
        if self.head is None:
            return True
        else:
            return False
        
    def display(self):
        """Traverse through the All element in Queue and display it."""
        if self.head is None:
            print("| Queue is Empty |")
        elif self.head.next is None:
            print(self.head.element)
        elif self.head.next.next is None:
            print(self.head.element,end=" <- ")
            print(self.head.next.element)
        else:
            cur = self.head
            while cur is not None:
                if cur.next is not None:
                    print(cur.element,end=" <- ")
                else:
                    print(cur.element)
                cur = cur.next
            
    def peek_last(self):
        cur = self.head
        if cur is None:
            return "|Queue is Empty"


qu = Queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.enqueue(40)
qu.enqueue(50)
qu.enqueue(60)


print(qu.is_empty())
qu.display()