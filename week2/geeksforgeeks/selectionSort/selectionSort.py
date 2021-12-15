#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        
        minIndex=i
        for j in range (i,len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex=j 
        
        return minIndex
        
    
    def selectionSort(self, arr,n):
        #code here
        for i in range (len(arr)):
            min_index=self.select(arr,i)
            temp = arr[i]
            arr[i]= arr[min_index]
            arr[min_index]= temp
        
        return arr