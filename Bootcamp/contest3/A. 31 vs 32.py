# Not group 31 vs group 32.

# You are given a target number, k. Starting from either 31 or 32, you can apply these two operations any amount of times:

# Add 4 to the current number
# Subtract 1 from the current number
# You want to use the minimum operations possible to get from your start number to the target number. Print out what number you have to start with to have the minimum operations to reach to k.

# Input
# The first line contains a single integer t (1≤t≤103) — the number of test cases.

# The single line of each test case contains a single integer k(0≤k≤103).

# Output
# For each of the t test cases, print out either "31" or "32" (without the quotes)
import sys
input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
 
    
t = inp()
 
def group3132(n):
    if n < 36 and n != 32 :
        return 31
        
    if n%4 == 0:
        return 32
    else :
        return 31
 
for i in range (t):
    Input = inp()
    print(group3132(Input))