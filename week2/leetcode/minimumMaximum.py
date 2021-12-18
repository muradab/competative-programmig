class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs = []
        
        for i in range(len(nums)//2):
            pairs.append([nums[i], nums[-1-i]])
        print(pairs)
        Max = sum(pairs[0])
        for j in pairs:
            Sum =  sum(j)
            if Sum > Max:
                Max = Sum
        return Max
            
        