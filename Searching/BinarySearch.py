
""" 
Iterative Algorithm:
    BinarySearch():
        Repeat unti low <= high:
            mid = low + (high-low)//2
            if arr[mid] == item:
                return mid
            else if arr[mid] < item:
                Set low = mid + 1
            else:
                Set high = mid - 1
"""

""" 
Recursive Algorithm:
    BinarySearch(arr, item, low, high):
        if low <= high:
            mid = low + (high-low)//2
            if arr[mid] == item:
                return mid
            else if arr[mid] < item:
                Call recursively BinarySearch(arr, item, mid+1, high)
            else:
                Call recursively BinarySearch(arr, item, low, mid-1)
"""

""" 
Best Case Time Complexity - O(1) 
Worst Case Time Complexity - O(logn) 
Average Case Time Complexity - O(logn) 

Auxilary Space - O(1) 
"""

class BinarySearch:         
    def binarySearchIterative(self,arr,n,item):
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid] == item:
                return mid
            elif arr[mid] < item:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1
                
    def binarySearchRecursive(self,arr,item,low,high):
        if low <= high:
            mid = low + (high-low)//2
            if arr[mid] == item:
                return mid
            elif arr[mid] < item:
                return self.binarySearchRecursive(arr,item,mid+1,high)
            else:
                return self.binarySearchRecursive(arr,item,low,mid-1)
        else:
            return -1
            
    # Output of program 3
        
if __name__ == "__main__":
    arr = [2,3,4,5,6,7,8,9]
    n = len(arr)
    binarySearch = BinarySearch()
    print(binarySearch.binarySearchIterative(arr,n,5))
    print(binarySearch.binarySearchRecursive(arr,5,0,n-1))