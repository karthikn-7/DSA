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
        self.queue[self.front] = None
        self.front += 1

    def peek(self)->any:
        """Returns the first element of the queue"""
        if self.queue:
            ...
        else:
            raise Exception("Queue is Empty")

    def display(self)->None:
        """Traverse through the all elementts and print out."""
        print(self.queue)

    
if __name__ == "__main__":
    cq = Queue(5)

    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.enqueue(40)
    cq.enqueue(40)

    cq.dequeue()

    cq.enqueue(50)

    cq.dequeue()

    cq.enqueue(60)
    print()
    cq.display()
