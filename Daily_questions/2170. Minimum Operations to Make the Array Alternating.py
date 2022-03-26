# You are given a 0-indexed array nums consisting of n positive integers.

# The array nums is called alternating if:

# nums[i - 2] == nums[i], where 2 <= i <= n - 1.
# nums[i - 1] != nums[i], where 1 <= i <= n - 1.
# In one operation, you can choose an index i and change nums[i] into any positive integer.

# Return the minimum number of operations required to make the array alternating.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return 0
        odd_indices = {}
        even_indices = {}
#         hint one : keep count
        for i in range(0,len(nums),2):
            if nums[i] not in even_indices:
                even_indices[nums[i]] = 1
            else :
                even_indices[nums[i]] += 1
                
        for i in range(1,len(nums),2):
            if nums[i] not in odd_indices:
                odd_indices[nums[i]] = 1
            else :
                odd_indices[nums[i]] += 1          
#       hint two :  maximize the keep elements 
        freq_even = (None,0)
        sec_freq_even = (None,0)
    
        for even in even_indices:
            if freq_even[1] < even_indices[even]:
                sec_freq_even = freq_even
                freq_even= (even , even_indices[even])
            elif sec_freq_even[1] < even_indices[even]:
                sec_freq_even = (even , even_indices[even])
        
        freq_odd = (None,0)
        sec_freq_odd = (None,0)
    
        for odd in odd_indices:
            if freq_odd[1] < odd_indices[odd]:
                sec_freq_odd = freq_odd
                freq_odd= (odd , odd_indices[odd])
            elif sec_freq_odd[1] < odd_indices[odd]:
                sec_freq_odd = (odd , odd_indices[odd])
#         hint 3 : different combinations
        if freq_even[0] != freq_odd[0]:
            return len(nums) - freq_even[1] - freq_odd[1]
        return len(nums) - max(freq_even[1] + sec_freq_odd[1] , freq_odd[1] + sec_freq_even[1] ) 
        
        
        
