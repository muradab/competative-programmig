# Selecting a good second question can be hard.
#  You want more than half of the students to be 
# able to comfortably answer the question but you don't want it to be so easy 
# that no one is challenged by it.

# You have n questions that you're considering and the i-th question
#  has a difficulty of ai. You also have m students in the contest 
# and the j-th student can comfortably solve a question of bj difficulty or less.
#  You want to see which questions would be good second questions for the contest
import sys
import math
input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
    
questions , students = invr()
 
ability = inlt()
ability.sort(reverse = True)
def goodQuestion (difficulty , ability,students):
    mid = len(ability) // 2
    
        
    
    if difficulty <= ability[mid] and difficulty > ability[-1]:
        
        print("YES")
    else :
        
        print( "NO")
       
for i in range (questions):
    difficulty = inp()
    goodQuestion (difficulty , ability,students)