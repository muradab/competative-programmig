# Vasiliy likes to rest after a hard work, so you may often meet him in some bar nearby. As all programmers do, he loves the famous drink "Beecola", which can be bought in n different shops in the city. It's known that the price of one bottle in the shop i is equal to xi coins.

# Vasiliy plans to buy his favorite drink for q consecutive days. He knows, that on the i-th day he will be able to spent mi coins. Now, for each of the days he want to know in how many different shops he can buy a bottle of "Beecola".

# Input
# The first line of the input contains a single integer n (1 ≤ n ≤ 100 000) — the number of shops in the city that sell Vasiliy's favourite drink.

# The second line contains n integers xi (1 ≤ xi ≤ 100 000) — prices of the bottles of the drink in the i-th shop.

# The third line contains a single integer q (1 ≤ q ≤ 100 000) — the number of days Vasiliy plans to buy the drink.

# Then follow q lines each containing one integer mi (1 ≤ mi ≤ 109) — the number of coins Vasiliy can spent on the i-th day.

# Output
# Print q integers. The i-th of them should be equal to the number of shops where Vasiliy will be able to buy a bottle of the drink on the i-th day.
import sys
 
 
input = sys.stdin.readline
 
number_of_shops = int(input())
 
prices_of_shop = list(map(int,input().split()))

prices_of_shop.sort()
 
number_of_days = int(input())
 
 
for i in range(number_of_days):
     coin = int(input())
     
     
     l = 0
     r = len(prices_of_shop) - 1
     
     while l <= r :
          mid = l + (r-l)//2
          
          if prices_of_shop[mid] <= coin:
               l = mid + 1
          else :
               r = mid - 1
     
     print(l)