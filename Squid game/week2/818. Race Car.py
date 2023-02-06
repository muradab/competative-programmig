class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 0, 1)])
        while queue:
            steps, position, speed = queue.popleft()
            if position == target:
                return steps
            queue.append((steps+1, position+speed, speed*2))
            
            if position + speed > target and speed > 0:
                queue.append((steps+1, position, -1))
                
            if position + speed < target and speed < 0:
                queue.append((steps+1, position, 1))
