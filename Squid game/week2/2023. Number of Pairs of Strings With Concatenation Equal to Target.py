class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        hashmap = defaultdict(set)
        for i in range(1, len(target)):
            pair = target[:i]
            word = target[i:]
            hashmap[pair].add(word)
            hashmap[word].add(pair)
        words = Counter()
        ans = 0
        
        for num in nums:
            
            for word in hashmap[num]:
                if word in words:
                    ans += words[word]
                    if word + num == num + word:
                        ans += words[word]
            words[num] += 1
        return ans 
