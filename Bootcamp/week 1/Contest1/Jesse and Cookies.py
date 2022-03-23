# Jesse loves cookies and wants the sweetness of some cookies to be greater than value . To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

# sweetness  Least sweet cookie   2nd least sweet cookie).

# This occurs until all the cookies have a sweetness .

# Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return .

# Example


# The smallest values are .
# Remove them then return  to the array. Now .
# Remove  and return  to the array. Now .
# Remove , return  and .
# Finally, remove  and return  to . Now .
# All values are  so the process stops after  iterations. Return .

# Function Description
# Complete the cookies function in the editor below.

# cookies has the following parameters:

# int k: the threshold value
# int A[n]: an array of sweetness values
# Returns

# int: the number of iterations required or 
# Input Format

# The first line has two space-separated integers,  and , the size of  and the minimum required sweetness respectively.

# The next line contains  space-separated integers, .


#!/bin/python3
import heapq
import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    operations = 0
    heapq.heapify(A)
    while (len(A)>=2 and A[0]<k):
        Sum = heapq.heappop(A)
        Sum += 2 *heapq.heappop(A)
        heapq.heappush(A,Sum)
            
        operations += 1
        
    if A[0] < k:
            return -1
        
    return operations 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
