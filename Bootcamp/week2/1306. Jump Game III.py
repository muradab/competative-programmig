# https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def inBound(index):
            if (0 <= index < len(arr) ):
                return True 
            return False
        def isZero(index):
            if inBound(index) and arr[index] == 0:
                return True
            return False
        
        
        visited = set()
        queue = deque()
        queue.append(start)
        
        while queue :
            size = len(queue)
            for i in range(size):
                popped = queue.popleft()
                if inBound(popped - arr[popped]) and (popped - arr[popped]) not in visited:
                    queue.append(popped - arr[popped])
                if inBound(popped + arr[popped]) and (popped + arr[popped]) not in visited:
                    queue.append(popped + arr[popped])
                
                    
                visited.add(popped)
                if isZero(popped):
                    return True
                
            
            
        return False    
            
            
        
