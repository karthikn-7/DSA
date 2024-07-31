class Searching_algorithm:

    def __init__(self, element, array) -> None:
        """Initialize element to find"""
        self.element = element
        self.array = array


    def linear_search(self):
        """Search through all element best:O(1), worst:O(n) if the element found returns it index
        else return -1"""
        count = 0
        for i in range(len(self.array)):
            if self.array[i] == self.element:
                return i,count
            count += 1
        return -1

    def binary_search(self):
        """Binary seach. which is only works on the sorted array more efficient than
        linear search, return tuple (index,iterations)"""

        left = 0
        right = len(self.array) - 1

        count = 0
        while left <= right:
            mid = (left + right) // 2
            
            if self.array[mid] == self.element:
                return mid, count
            
            if self.array[mid] < self.element:
                left = mid + 1
            
            if self.array[mid] > self.element:
                right = mid - 1
            
            count += 1
            
        return -1, count

            

if __name__ == "__main__":

    array = [2,4,7,9,11,13,16,21]

    sa = Searching_algorithm(21, array)
    
    bs = sa.binary_search()
    ls = sa.linear_search()

    print(bs)
    print(ls)