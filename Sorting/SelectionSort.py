
""" 
Best Case Time Complexity- O(n^2)
Worst Case Time Complexity - O(n^2)
Average Case Time Complexity - O(n^2)
Auxilary Space- O(1)
Stable - Can be made stable below implementation is not stable
Sorting In Place - Yes

Best Case occurs when array is already sorted.
Worst Case occurs when array is reverse order.
Average case occurs when array is neither in ascending order nor in descending order i.e, jumbled order.
"""

class SelectionSort:
    def __init__(self, array, length):
        self.array = array
        self.length = length
        
    def selectionSort(self):
        for i in range(0, self.length):
            self.minimum = i
            for j in range(i+1, self.length):
                if self.array[self.minimum] > self.array[j]:
                    self.minimum = j
                    
            self.array[i], self.array[self.minimum] = self.array[self.minimum], self.array[i]
            
    def printArray(self):
        print("Sorted array is: ")
        for i in range(0,self.length):
            print(self.array[i], end=" ")
            
if __name__ == '__main__':
    data = [0,-2,50,70,20]
    selectionSortObj = SelectionSort(data, len(data))
    selectionSortObj.selectionSort()
    selectionSortObj.printArray()