class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        monoStack = []
        
        Dict = dict()
        result = []
       
        
        for i in  nums2 :
            if len(monoStack)==0:
                monoStack.append(i)
            elif monoStack[-1] > i :
                monoStack.append(i)
            else :
                while  len(monoStack) >0 and monoStack[-1] < i :
                    Dict[monoStack.pop()] = i
                    
                monoStack.append(i)
        for i in nums1:
            if i in Dict:
                result.append(Dict[i])
            else:
                result.append(-1)
                
        return result
                
                
               
        
                
                
                    
                    
                
                            