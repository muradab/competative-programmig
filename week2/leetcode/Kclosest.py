import math
class Solution:
    def calculateSqrt(self, i):
        ans = math.sqrt(i[0]**2 + i[1]**2)
        return ans
    
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: self.calculateSqrt(x))
        return points[0:k]
        '''
        distanceList = []
        for i in range (len(points)):
            distance = math.sqrt((points[i][0]**2 + points[i][1]**2))
            distanceList.append(distance)
                        
        for i in range(len(distanceList)):
            for j in range(len(distanceList)-1):
                if (distanceList[j] > distanceList[j + 1]) :
                    temp = distanceList[j]
                    temp2 = points[j]
                    distanceList[j] =  distanceList[j+ 1]
                    points[j] =  points[j+ 1]
                    distanceList[j+1] = temp
                    points[j+1] = temp2
                    
        return points[:k]
        
        '''
       
       
   

   
        
                        