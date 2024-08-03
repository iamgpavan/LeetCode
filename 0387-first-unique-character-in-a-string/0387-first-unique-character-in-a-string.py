from collections import deque 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = [0]*26
        dq = deque([])
        i = 0
        
        while(i < len(s)):
            ind = ord(s[i]) - ord('a') 
            # O(1) operation
            if(hashmap[ind] == 0):
                dq.append(i)
            hashmap[ind] += 1
            
            while((len(dq)) and hashmap[ord(s[dq[0]]) - ord('a')] > 1):
                # O(1) operation
                dq.popleft()
            
            i += 1
        
        if(not len(dq)):
            return -1
        
        return dq[0]
        