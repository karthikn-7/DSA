class Stack:
    """Stack data structure,last inserted element will come out first
    lifo - last in first out."""

    def __init__(self,size):
        self.stack = [None]*size
        self.pointer = -1

    def push(self,element:any)->None:
        """Insert the new element in the stack,insert at the last"""
        if self.pointer < len(self.stack)-1:
            self.pointer += 1
            self.stack[self.pointer] = element

        else:
            raise Exception("Stack is full!")

    def pop(self)->None:
        """Remove last element from the stack"""
        if not self.is_empty():
            self.stack[self.pointer] = None
            self.pointer -= 1
        else:
            raise Exception("Stack is empty!")


    def peek(self)->any:
        """Returns the last element"""
        return self.stack[self.pointer]

    def is_empty(self)->bool:
        """Checks if the stack is empty if it is return true.else return false"""
        if self.pointer == -1:
            return True
        return False

    def is_full(self)->bool:
        """Return boolean, if the stack is full return true, else returns false"""
        if self.pointer == len(self.stack)-1:
            return True
        return False

    def display(self):
        """Traverse throught the stack and printouts the all element from the begining of the stack."""
        for i in range(self.pointer,-1,-1):
            print("|",self.stack[i],"|")





st = Stack(6)

st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.push(60)



st.display()
