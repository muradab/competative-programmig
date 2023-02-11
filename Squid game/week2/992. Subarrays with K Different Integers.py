class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        '''
        solution 
            find subarrays with at most K distnict subarrays
            then find subarrays with atmost k-1 distnict characters
            finally the difference between these two will led to subarray with exactly k distnict subarray 
        '''
        def count(k):
            hashmap = Counter()
            right = left = ans = 0
            while right < len(nums):
                hashmap[nums[right]] += 1
                while len(hashmap) > k:
                    hashmap[nums[left]] -= 1
                    if not hashmap[nums[left]]:
                        del hashmap[nums[left]]
                    left += 1
                
                ans += right - left + 1
                right += 1
            return ans
        return count(k) - count(k-1)
                    
