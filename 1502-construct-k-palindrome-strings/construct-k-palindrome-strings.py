class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if(len(s) < k):
            return False

        hashnumber = 0

        for char in s:
            # hashmap[ord(char)-ord('a')] += 1
            hashnumber = hashnumber ^ (1<<(ord(char)-ord('a')))
        
        cnt = 0

        for i in range(26):
            if(hashnumber & (1<<i)):
                cnt += 1
        
        if(cnt > k):
            return False
        
        return True
        
