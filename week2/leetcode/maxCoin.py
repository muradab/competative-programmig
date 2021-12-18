class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins = 0
        print(piles)
        for i in range(1,len(piles)):
            if (i % 3 == 2 ):
                coins += piles[-1]
                print(piles[-1])
                piles.pop()
                
            elif (i % 3 == 0 ):
                if len(piles) == 0:
                    break
                else :
                    piles.pop(0)
                
            else :                
                piles.pop()
          
            
            
            
        return coins
        
