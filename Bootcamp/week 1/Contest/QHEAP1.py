# QHEAP1locked
# Problem
# Submissions
# This question is designed to help you get a better understanding of basic heap operations.

# There are  types of query:

# " " - Add an element  to the heap.
# " " - Delete the element  from the heap.
# "" - Print the minimum of all the elements in the heap.
# NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.
import heapq
lengthOfInput = int(input())
array = []
willBePoppped = {}

for i in range(lengthOfInput):
    mainInput = [int(x) for x in input().split()]
    if mainInput[0] == 1:
        heapq.heappush(array,mainInput[1])
    elif mainInput[0] == 2:
        if mainInput[1] == array[0]:
            heapq.heappop(array)
            while len (array) > 0 and array[0] in willBePoppped and willBePoppped[array[0]] > 0:
                willBePoppped[array[0]] -= 1 
                heapq.heappop(array)
                    
        else:
            if mainInput[1] in willBePoppped:
                willBePoppped[mainInput[1]] += 1
            else:
                willBePoppped[mainInput[1]] = 1
     
    elif mainInput[0] == 3:
        print(array[0])