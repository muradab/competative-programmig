class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        checkdigit = lambda log : log.split()[1].isdigit()
        digitlogs = []
        letterlogs = []
        for log in logs:
            if checkdigit(log):
                digitlogs.append(log)
            else:
                letterlogs.append(log)
        letterlogs.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        return letterlogs + digitlogs
                        
