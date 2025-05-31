class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        n = len(s)

        for char in t:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        distinct = len(d)

        # Assuming t is present in entire s
        start = 0
        end = n

        # start = i and end = j and started to explore on s
        i = 0
        j = 0

        while(j < n):
            if(s[j] in d):
                d[s[j]] -= 1

                if(d[s[j]] == 0):
                    distinct -= 1
                
                while(distinct == 0):
                    if((j-i+1) < (end-start+1)):
                        start = i
                        end = j
                    
                    if(s[i] in d):
                        d[s[i]] += 1

                        if(d[s[i]] == 1):
                            distinct += 1
                    
                    i += 1 
            j += 1

        if(end == n):
            return ""
        
        return s[start:end+1]
        