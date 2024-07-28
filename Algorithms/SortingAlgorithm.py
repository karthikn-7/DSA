 
class SortingAlgorithms:

    def counting_sort(self, array):
        max_element = max(array)
        count_array = [0] * (max(array)+1)

        for num in array:
            count_array[ num ] = count_array[ num ] + 1


        for i in range(1,max_element+1):
            count_array[i] = count_array[i] + count_array[i-1]


        output_array = [0]*(len(array))
        for i in range(len(array)-1, -1, -1):
            output_array[count_array[array[i]]-1] = array[i]
            count_array[array[i]] -= 1


        return output_array

    def bubble_sort(self,array):
        for i in range(len(array)):
            swapped = False
            for j in range(len(array)-1):
                if array[j] > array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
                    swapped = True

            if not swapped:
                return array

        return array

sa = SortingAlgorithms()


array = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
gfg_array = [2,5,3,0,2,3,0,3]


sa.bubble_sort(gfg_array)

result = {
    "counting_sort":sa.counting_sort(array),
    "bubble_sort":sa.bubble_sort(array)
    }

print(result)

