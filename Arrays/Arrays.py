# Pending
class Arrays:
    def __init__(self, size):
        self.array = [0]*size
        self.array_size = 0


    def traverse_array(self,array):
        length = len(array)
        for i in range(length):
            print(array[i])

    def insert_at_beginning(self,element):

        if self.array_size < len(self.array):
            for i in range(len(self.array)-1,-1,-1):
                self.array[i] = self.array[i - 1]

            self.array_size += 1
            self.array[0] = element


        else:
            raise IndexError("Array is full!")

    def insert_at_position(self, index, element):

        if self.array_size < len(self.array):
            for i in range( len(self.array)-1,index,-1 ):
                self.array[i] = self.array[i-1]

            self.array[index] = element
            self.array_size += 1
        else:
            raise IndexError("Array is full")

    def insert_at_end(self,element):
        if self.array_size < len(self.array):

            for i in range(self.array_size,len(self.array)-1):
                self.array[i] = self.array[i+1]
                self.array[len(self.array)-1] = element

        else:
            raise IndexError("Array is full")


    def display_array(self):
        print("current array size:",self.array_size)
        print("array:",self.array)


a = Arrays(10)

a.insert_at_beginning(10)
a.insert_at_beginning(20)
a.insert_at_beginning(30)
a.insert_at_beginning(40)
a.insert_at_beginning(50)
a.insert_at_beginning(60)



a.insert_at_position(0,"in first position")

a.insert_at_end(200)
a.insert_at_end(300)
a.insert_at_end(400)
a.insert_at_end(500)

a.display_array()
