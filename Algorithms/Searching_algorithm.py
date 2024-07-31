class Searching_algorithm:

    def __init__(self, element) -> None:
        """Initialize element to find"""
        self.element = element


    def linear_search(self,array):
        """Search through all element best:O(1), worst:O(n) if the element found returns it index
        else return -1"""
        for i in range(len(array)):
            if array[i] == self.element:
                return i
        return -1
            

if __name__ == "__main__":

    array = [11,22,33,20,33,1]

    sa = Searching_algorithm(11)
    result = sa.linear_search(array)

    print(result)