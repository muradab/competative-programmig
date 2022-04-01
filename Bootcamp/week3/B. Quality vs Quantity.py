# https://codeforces.com/problemset/problem/1646/B


import sys
input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
 
 
# The first line of each test case contains an integer n (3≤n≤2⋅105) — the length of the given sequence.
 
# The second line of each test case contains n integers a1,a2,…,an (0≤ai≤109) — the given sequence.
 
# It is guaranteed that the sum of n over all test cases does not exceed 2⋅105.
 
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
 
 
test_cases = inp()
 
for _ in range (test_cases):
    
    length = inp()
    
    inputs = inlt()
    inputs.sort()
    
    left = 1
    right = length - 1
    
    blue = inputs[0]
    red = 0
    
    while left < right :
        blue += inputs[left]
        red += inputs[right]
        
        if blue < red :
            print("YES")
            break
        
        left += 1
        right -= 1
    if  blue >= red :    
        print("NO")
