
class Node:
    def __init__(self, data):
        self.prev = None
        self.element = data
        self.pointer = None


class DoublyLinkedList:
    """
    'Doubly linked list'
    It stores the data uncontigiously in memory.
    Efficient insertion, deletion
    Unlike singly linked list it can also traverse through backwards of the list
    -Karthikn
    """
    def __init__(self):
        self.head = None

    def add_element(self, data: any)->None:
        """
        Parameters: data
        Add the elements in the list
        Supports any data type
        """
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)

            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer


            cur.pointer = new_node
            new_node.prev = cur


    def traverse(self) -> None:
        """
        Traverse through the all element from the list and prints it.
        """
        cur = self.head
        print("[",end = "")
        while cur is not None:
            if cur.pointer is not None:
                print(cur.element, end = " ")
            else:
                print(cur.element, end = "")
            cur = cur.pointer
        print("]")

    def remove_element(self,element: any) -> None:
        """
        Remove the all element from the list which matches to the element
        """
        if self.head.element == element:
            self.head = self.head.pointer
            self.head.prev = None

        else:
            cur = self.head
            while cur.pointer is not None:#if cur is not none it will run the iteration

                if cur.pointer.element == element:#if the current node's pointerelement is equals to element
                    cur.pointer = cur.pointer.pointer #current node's pointer = node's pointer's pointer

                     # if the element to remove is last element of the list it might throw error so checking for pointer is not none
                     # if it is none no need to change the pointer's  previous to current node.
                    if cur.pointer is not None:
                        cur.pointer.prev = cur

                # setting the cur variable's data to current
                # node's pointer node
                cur = cur.pointer

    def length(self)-> int:
        """
        Returns the length of the list
        """
        cur = self.head
        count = 1
        while cur.pointer is not None:
            cur = cur.pointer
            count +=1
        return count

    def search_element(self, element:any) -> int:
        """
        Return the index of the element,
        If not found returns -1
        """
        cur = self.head
        count = 0
        while cur.pointer is not None:
            if cur.element == element:
                return count
            count+=1
            cur = cur.pointer

        return -1

    def insert_at(self, index:int, data:any) -> None:
        """
        Insert the new element at the specified index.
        """
        if index < 0:
            raise IndexError("Invalid index")
        elif index == 0: # if the index is zero
            new_node = Node(data) # New node creation

            if self.head is not None:
                new_node.pointer = self.head # New node pointer is pointing to current head
                self.head.prev = new_node # Previos of head is set to new node
            self.head = new_node #self.head is now new node
        else:
            cur = self.head
            count = 0

            while cur is not None and count < index -1:
                cur = cur.pointer
                count +=1

            if cur is None:
                raise IndexError("Invalid index")
            else:
                new_node = Node(data)
                new_node.prev = cur
                new_node.pointer = cur.pointer
                cur.pointer = new_node
                if new_node.pointer is not None:
                    new_node.pointer.prev = new_node

    def update_element(self, index:int, new_element:any) -> None:
        """
        Update the element at the specific index
        """
        cur = self.head
        if index < 0:
            raise IndexError("Invalid index")


        count = 0
        while cur is not None and index != count:
            cur = cur.pointer
            count +=1

        if cur is not None:
            cur.element = new_element
            return
        raise IndexError("Invalid index")

    def clear_list(self) -> None:
        """Clears all the element in the list"""
        self.head = None
        
    def reverse(self):
        """Reverse the list and return none, to view the reverse traversal,
        call this method before the traverser method"""
        cur = self.head
        last_node = None
        while cur is not None:
            temp = cur.prev
            cur.prev = cur.pointer
            cur.pointer = temp
            if cur.prev is None:
                last_node = cur
            cur = cur.prev
            
        self.head = last_node





dll = DoublyLinkedList()
dll.add_element(0)
dll.add_element(10)
dll.add_element(20)
dll.add_element(30)
dll.add_element(40)


print("List:",end="")
dll.traverse()

dll.reverse()

print("Reversed List:",end="")
dll.traverse()


# print("Element found at:",dll.search_element(20))
# print("length of the list is:",dll.length())


