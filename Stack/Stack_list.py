import SinglyLinkedList

sl = SinglyLinkedList.Linked_list()


class Stack:
    def push(self,element:any):
        sl.add_element(element)

    def pop(self):
        try:
            sl.remove_at_first()
        except:
            print("Stack is empty |__|")
            
    
    def peek(self):
        print("Last element",sl.show_tail())
            
    
    def show_stack(self):
        try:
            
            sl.traverse()
        except:
            print("Stack is empty |__|")
            
    
st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.push(60)
st.push(70)
st.push(80)

st.pop()
st.pop()

st.peek()

st.show_stack()