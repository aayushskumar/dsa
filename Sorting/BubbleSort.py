
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

class BubbleSort:
    def __init__(self, array, length):
        self.array = array
        self.length = length
        
    def bubbleSort(self):
        for i in range(0, self.length):
            self.swapped = True
            for j in range(0, self.length - 1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    self.swapped = False
                    
            if self.swapped:
                break
            
    def printArray(self):
        print("Sorted array is: ")
        for i in range(0,self.length):
            print(self.array[i], end=" ")
            
if __name__ == '__main__':
    data = [0,-2,50,70,20]
    bubbleSortObj = BubbleSort(data, len(data))
    bubbleSortObj.bubbleSort()
    bubbleSortObj.printArray()