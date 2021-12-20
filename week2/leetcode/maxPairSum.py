class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        myDict = dict()
        operations = 0
        
     
        for i in nums :
            if i  in myDict :
                myDict[i] += 1
                
            else :
                myDict[i] = 1
        for key in myDict :
            while myDict[key] > 0:
                if k - key == key and myDict[key]<2:
                    break
                    
                
                elif k-key in myDict and myDict[k-key] > 0 :
                   
                    operations += 1
                   
                    myDict[key] -= 1
                    myDict[k-key] -= 1
                else :
                    break
           
                

        return operations
        
        