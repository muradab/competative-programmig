class Solution:
    def minOperations(self, logs: List[str]) -> int:
        current = 0
        for log in logs:
            if log == '../':
                current = max(0, current-1)
            elif log != './':
                current += 1
        return current
                
        
