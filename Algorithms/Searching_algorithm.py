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
    

    def exponential_search(self):
        """Exponential search its very efficient 
        for large number of elements present in the array"""
        count = 0
        if not self.array:
            return (-1,count)

        if self.element < self.array[0]:
            return (-1 , count)
        
        if self.array[0] == self.element:
            return (0, count)
        
        bound = 1
        
        while bound < len(self.array) and self.array[bound] < self.element:
            bound *= 2
            count += 1
        print(bound,len(self.array))

        right = min( bound, len(self.array)-1 )
        if self.array[right] == self.element:
            return (right,count)
        
        left = bound// 2
        return self.__bs_exponential(self.element,left,right,count)
        

    def __bs_exponential(self,target,left,right,count):
        "Exponential search utility method"
        
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == target:
                return (mid,count)
            if self.array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            count += 1
        return -1


if __name__ == "__main__":

    array = [2,4,7,9,11,13,16,21,23,25,27,33,66,78,89,98,99,111,123,134,145,156,157,158,177,198,275,344,345]

    sa = Searching_algorithm(123, array)
    
    bs = sa.binary_search()
    ls = sa.linear_search()
    es = sa.exponential_search()

    print("Exponential Search:",es)
    print("Binary Search:",bs)