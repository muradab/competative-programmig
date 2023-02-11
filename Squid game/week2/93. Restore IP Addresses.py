class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(index, needed, path):
            if needed < 0:
                return 0
            if index == len(s):
                if needed == 0:
                    result.append('.'.join(path))
                return
            if s[index] =='0':
                dfs(index+1, needed-1, path+['0'])
                return
            for j in range(3):
                if index + j < len(s) and int(s[index:index+j+1]) <= 255:
                    dfs(index+j+1, needed-1, path+[s[index:index+j+1]])
        result = []
        dfs(0, 4, [])
        return result
            
                
                
                
