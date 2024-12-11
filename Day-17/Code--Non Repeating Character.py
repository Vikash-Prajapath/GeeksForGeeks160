class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        seen = set()
        repeat = set()
        
        for i in s:
            if i in seen:
                repeat.add(i)
            else:
                seen.add(i)
                
        for i in s:
            if i not in repeat:
                return i
                
        return -1
