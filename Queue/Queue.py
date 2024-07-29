class Queue:
    """This is Queue data structure that is implemented using Array,
    when compared to implementing using list,array is not efficient"""
    
    def __init__(self,size):
        """Initializing the queue with the given size."""
        self.max = size
        self.queue = [None]*size
        null = -1
        self.front = self.rear = null
        
    def enqueue(self,element):
        """Adds the elements in the end of the queue"""
        if self.front == -1 and self.rear == -1:
            self.front += 1
            self.rear += 1
            self.queue[self.rear] = element
            return
        
        if self.rear == self.max-1 and self.front == 0 or self.front - 1 == self.rear:
            raise Exception("Queue is full")
        
        
        if self.rear == self.max-1 and self.front != 0:
            self.rear = 0
            self.queue[self.rear] = element
            return
        
        
        self.rear += 1
        self.queue[self.rear] = element
            
            
            

    def dequeue(self)->None:
        """Removes the front element from the queue"""
        if self.front == self.rear:
            raise Exception("Queue is Empty")
            
        if self.front != self.max -1:
            self.queue[self.front] = None
            self.front += 1
            return
        
        if self.front == self.max -1:
            self.queue[self.front] = None
            self.front = 0

    def peek(self)->any:
        """Returns the first element of the queue"""
        if self.queue:
            ...
        else:
            raise Exception("Queue is Empty")

    def display(self)->None:
        """Traverse through the all elementts and print out."""
        if self.front == -1 and self.rear == -1:
            print("Queue is Empty")
            return
        
        i = self.front
        

        if self.front == 0 and self.rear == 0:
            print(self.queue[i])
            return
        elif self.front <= self.rear:
            for i in range(self.front , self.rear+1):
                if i != self.rear:
                    print(self.queue[i],end=" <- ")
                else:
                    print(self.queue[i])
        else:
            while i != self.rear:
                print(self.queue[i],end=" <- ")
                if i == self.max-1:
                    i = 0
                    print(self.queue[i],end=" <- ")
                i += 1
            print(self.queue[i])

    def show_front(self) -> any:
        "Returns the first element of the queue,if the queue is empty return false"
        if self.front == 0 and self.rear == 0:
            return self.queue[self.front]
        if self.front == -1 or self.front == self.rear:
            return False
        return self.queue[self.front]
    
    def show_last(self) -> any:
        "Returns the last element of the queue,if the queue is empty return false"
        if self.front == 0 and self.rear == 0:
            return self.queue[self.rear]
        if self.rear == -1 or self.front == self.rear:
            return False
        return self.queue[self.rear]


    
if __name__ == "__main__":
    cq = Queue(5)

    cq.enqueue("first element")
    cq.enqueue("second element")
    cq.enqueue("third element")
    cq.enqueue("fourth element")
    cq.enqueue("fifth element")

    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()

    cq.enqueue("new first element")
    cq.enqueue("new second element")
    cq.enqueue("new third element")
    cq.enqueue("new fourth element")

    cq.dequeue()
    
    cq.enqueue("new fifth element")


    print(cq.show_front())
