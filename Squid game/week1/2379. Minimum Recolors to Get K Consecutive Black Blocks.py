class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        operations = 0
        result = float('inf') 
        
        for right in range(len(blocks)):
            if blocks[right]=='W':
                operations += 1
            
            if right-left+1 == k:
                result = min(result, operations)
                if blocks[left]=='W':
                    operations -= 1
                left += 1                
        
        return result
