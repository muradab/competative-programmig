#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
         leftChild = self.leftChild(i)
         rightChild = self.rightChild(i)
         
         minimum = i 
        
         
         if leftChild <= n-1 and arr[leftChild] > arr[minimum]:
             minimum = leftChild
          
         if rightChild <= n-1 and arr[rightChild] > arr[minimum]:
             minimum = rightChild
        
         if minimum != i :
             arr[i],arr[minimum] = arr[minimum],arr[i]
             
             self.heapify(arr,n,minimum)
            
       
       
        
                
            
                
                
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range((n-1),-1,-1):
            self.heapify(arr,n,i)
            
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        
        
        
        for i in range(n):
        
            arr[n-1-i],arr[0] = arr[0],arr[n-1-i]
            
            self.heapify(arr,n-1-i,0)

        print(arr,len(arr))
            
             
            
    
    # Function to get parent
    def getParent(self,i):
        return (i-1)//2
    
    def leftChild(self,i):
        left_index = 2 * i  +1
        return left_index
        
    
    def rightChild(self,i):
        right_index = 2 * i + 2
        return right_index
        
        
    # Function to get maximum
    def getMax(self,arr):
        return arr[0]
        
    # Function to get left child

s = Solution()

n = 146

input = "932 66 777 426 127 404 63 281 426 317 735 628 543 78 31 811 626 104 389 412 687 296 35 252 441 675 604 770 342 284 917 274 702 46 53 829 450 116 463 229 786 198 857 329 276 888 140 254 992 530 18 31 178 405 284 619 80 240 742 423 876 659 49 931 57 102 760 859 571 575 88 357 773 945 38 401 186 531 655 530 413 673 562 591 79 198 563 159 790 305 582 666 316 984 597 373 86 710 584 9 285 673 718 411 970 757 812 508 288 468 39 701 493 953 644 924 151 559 84 293 864 18 959 532 2 909 257 441 619 842 802 256 515 521 667 837 630 832 346 918 652 385 971 145 690 967"

arr = input.split()
arr = list(map(int,arr))


s.HeapSort(arr,n)
    