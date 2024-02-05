class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = [0]*26
        
        for i in range(len(s)):
            arr[ord(s[i])-ord('a')] += 1
        
        for i in range(len(s)):
            if(arr[ord(s[i])-ord('a')] == 1):
                return i
        
        return -1