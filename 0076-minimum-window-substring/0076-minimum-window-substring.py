class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(s) < len(t)):
            return ""
        
        hm = {}
        
        for char in t:
            hm[char] = hm.get(char, 0) + 1
        
        count = len(hm)
        
        start = 0
        end = len(s)
        
        i = 0
        j = 0
        
        while(j < len(s)):
            if(s[j] in hm):
                hm[s[j]] -= 1
                
                if(hm[s[j]] == 0):
                    count -= 1
                
                while(count == 0):
                    if((end-start+1) > (j-i+1)):
                        end = j
                        start = i
                    
                    if(s[i] in hm):
                        # print(hm)
                        hm[s[i]] += 1
                        # print("After", hm)
                        if(hm[s[i]] == 1): ## VVIMP
                            count += 1
                    
                    i += 1
            
            j += 1
        
        if(end == len(s)):
            return ""
        
        return s[start:end+1]
        
        