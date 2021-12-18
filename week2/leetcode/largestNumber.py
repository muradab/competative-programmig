class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort()
       
        for i in range (len(nums)):
            for j in range(len(nums)-1):
                x1 = str(nums[j])*9
                x2 = str(nums[j+1])*9
                if x1[:9] < x2[:9]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp 
                elif(x1[:9] == x2[:9]):
                    if nums[j]<nums[j+1]:
                        temp = nums[j]
                        nums[j] = nums[j+1]
                        nums[j+1] = temp
                        
        while nums[0] == 0 :
            if len(nums)>1 :
                nums.pop(0)
            else:
                break
               
        return ''.join([str(element) for element in nums])
                    
                    
                    
                
            
            
                        
        
        