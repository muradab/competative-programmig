# You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].

# For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

# Implement the TopVotedCandidate class:

# TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
# int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.times = times
        
        counter = {persons[0]:1}
        
        self.leader = [persons[0]]
        
        for i in range (1,len(persons)):
            if persons[i] in counter:
                counter[persons[i]]+=1
            else:
                counter[persons[i]] = 1

            if counter[self.leader[-1]] > counter[persons[i]]:
                self.leader.append(self.leader[-1])
            else:
                self.leader.append(persons[i])
            
        
       
    
    def q(self, t: int) -> int:
        left = 0
        right = len(self.times)-1
        
        while left <= right:
            mid = left  + (right-left)//2
            
            if t < self.times[mid]:
                right = mid-1
                
            elif t > self.times[mid]:
                left  = mid + 1
            else:
                return self.leader[mid]
            
        if self.times[mid] > t:
            return self.leader[mid-1]
        return self.leader[mid]





# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
