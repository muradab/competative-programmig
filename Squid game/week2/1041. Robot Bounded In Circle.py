class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1
        for instruction in instructions:
            if instruction == 'R':
                dx, dy = dy, -dx
            elif instruction == 'L':
                dx, dy = -dy, dx
            else:
                x += dx
                y += dy
            
        return( x == 0 and y == 0) or not(dx == 0 and dy == 1)
