class Solution:
    def search(self, pat, txt):
        pat_len = len(pat)
        txt_len =  len(txt)
        result = []
        
        for i in range(txt_len - pat_len + 1):
            if txt[i:i+pat_len] == pat:
                result.append(i)
                
        return result
