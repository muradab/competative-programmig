class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pointsToAge = [[0,0]]+sorted((age, score) for score, age in zip(scores, ages))
        @lru_cache(None)
        def dp(index, prev):
            if index == len(pointsToAge):
                return 0
            use = 0
            if pointsToAge[index][1] >= pointsToAge[prev][1]:
                use = dp(index+1,index) + pointsToAge[index][1]
            skip = dp(index+1, prev)
            return max (skip , use)
        return dp(1, 0)
                    
