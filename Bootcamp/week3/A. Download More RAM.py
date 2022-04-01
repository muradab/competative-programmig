# https://codeforces.com/problemset/problem/1629/A

import sys
input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
 
 
# Input
# The first line of the input contains a single integer t (1≤t≤100) — the number of test cases. The description of test cases follows.
 
# The first line of each test case contains the integers n and k (1≤n≤100, 1≤k≤1000). Then two lines follow, each containing n integers describing the arrays a and b (1≤ai,bi≤1000).
 
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def invr():
    return(map(int,input().split()))
 
 
test_cases = inp()
 
for _ in range (test_cases):
    
    length , RAM = invr()
    
    
    
    software = inlt()
    permanent = inlt()
    
    Tuple = []
    
    for i in range(length):
        Tuple.append((software[i],permanent[i]))
        
    Tuple.sort()
    
    for t in Tuple:
        if RAM >= t[0]:
            RAM += t[1]
        else:
            break
    print(RAM)
