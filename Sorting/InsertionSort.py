
""" 
Best Case Time Complexity- O(n)
Worst Case Time Complexity - O(n^2)
Average Case Time Complexity - O(n^2)
Auxilary Space- O(1)
Stable - Yes
Sorting In Place - Yes

Best Case occurs when array is already sorted.
Worst Case occurs when array is reverse order.
Average case occurs when array is neither in ascending order nor in descending order i.e, jumbled order.
"""

class InsertionSort:
    def __init__(self, array, length):
        self.array = array
        self.length = length
        
    def insertionSort(self):
        for i in range(1, self.length):
            self.key = self.array[i]
            j = i-1
            while j >= 0 and self.key < self.array[j]:
                self.array[j+1] = self.array[j]
                j = j - 1
                    
            self.array[j+1] = self.key
            
    def printArray(self):
        print("Sorted array is: ")
        for i in range(0,self.length):
            print(self.array[i], end=" ")
            
if __name__ == '__main__':
    data = [0,-2,50,70,20]
    insertionSortObj = InsertionSort(data, len(data))
    insertionSortObj.insertionSort()
    insertionSortObj.printArray()
