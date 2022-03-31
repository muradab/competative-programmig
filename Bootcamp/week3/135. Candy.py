# https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
      
        ratings.append(-1)
        ratings.insert(0,-1)
        rating_tuple  = [] 
        
        for i in range (1,len(ratings)-1):
            rating_tuple.append((ratings[i],i))
            
        rating_tuple.sort()
        
        
        result = [0] *len(ratings)
       
        for rt in rating_tuple :
            idx = rt[1]
            val = rt[0]
            ans = 1
            if val > ratings[idx+1]:
                ans = max(ans, result[idx+1]+1)
            if val > ratings[idx-1]:
                ans = max(ans, result[idx-1]+1)
            
            result[idx]= ans

        return sum(result)
