# Limak is going to participate in a contest on the last day of the 2016. The contest will start at 20:00 and will last four hours, exactly until midnight. There will be n problems, sorted by difficulty, i.e. problem 1 is the easiest and problem n is the hardest. Limak knows it will take him 5·i minutes to solve the i-th problem.

# Limak's friends organize a New Year's Eve party and Limak wants to be there at midnight or earlier. He needs k minutes to get there from his house, where he will participate in the contest first.

# How many problems can Limak solve if he wants to make it to the party?

# Input
# The only line of the input contains two integers n and k (1 ≤ n ≤ 10, 1 ≤ k ≤ 240) — the number of the problems in the contest and the number of minutes Limak needs to get to the party from his house.

# Output
# Print one integer, denoting the maximum possible number of problems Limak can solve so that he could get to the party at midnight or earlier.
import sys
input = sys.stdin.readline
 
 
 
problems , time = (map(int,input().split()))
sum_ = time
solved = 0
 
while sum_ <= 240 and solved < problems:
     sum_ += (solved+1)*5 
     if sum_ <= 240 :
          solved += 1
print(solved)