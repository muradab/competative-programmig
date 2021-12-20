class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        myDict = dict()
        count = 0
        array = []
        for i in changed :
            if i  in myDict :
                myDict[i] += 1
                
            else :
                myDict[i] = 1
        for key in myDict :
            while myDict[key] != 0:
                if key*2 in myDict and myDict[key*2] > 0:
                    array.append(key)
                    myDict[key] -= 1
                    myDict[key*2] -= 1
                else :
                    return []

        return array

               
                            