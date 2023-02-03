class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splittedPath = path.split('/')
        for directory in splittedPath:
            if not directory or directory == '.':
                continue
            if directory == '..' :
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
        return '/'+'/'.join(stack)

               
