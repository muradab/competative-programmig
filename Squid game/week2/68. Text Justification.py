class Solution:
    # justifys the last line
    def leftJustify(self, start, end, maxWidth, word_len, words):
        string = []
        right_spaces = maxWidth - word_len
        right_spaces -= (end-start)
        
        while start < len(words):
            string.append(words[start])
            start += 1
           
        string = ' '.join(string)
        return string + ' '*right_spaces
        
    # justifies normal lines
    def lineJustify(self, start, end, maxWidth, word_len, words):
        cur_word = words[start]
        
        if start == end:
            left_spaces = maxWidth - len(cur_word)
            return cur_word + (' '*left_spaces)
        
        total_spaces = maxWidth - word_len
        word_count = end - start
        
        normal_spaces = total_spaces // word_count
        # extra spaces needed to make it balanced
        balancers = total_spaces % word_count
        
        string = []
        while start < end:
            string.append(words[start])
            new_spaces = ' ' * normal_spaces
            
            if balancers:
                new_spaces += ' '
                balancers -= 1
            string.append(new_spaces)
            start += 1
            
        string.append(words[end])    
        return ''.join(string)
            
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        start = 0
        cur_len = 0
        
        for i, word in enumerate(words):
            # check if it fits the line
            if cur_len + (i - start) + len(word) <= maxWidth:
                cur_len += len(word)
            
            # justify the line
            else:
                
                line = self.lineJustify(start, i-1, maxWidth, cur_len, words)
                cur_len = len(word)
                start = i
                output.append(line)
        
        # apply left justify to last line   
        if start < len(words):
            line = self.leftJustify(start, len(words)-1,  maxWidth, cur_len, words)
            output.append(line)
            
        return output
            
        
        
