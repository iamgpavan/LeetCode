class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        forward = [0]*len(s)
        backward = [0]*len(s) 

        for (start, end, direction) in shifts:
            if(direction == 1):
                forward[start] += 1
                if(end < len(s)-1):
                    forward[end+1] -= 1
            else:
                backward[start] += 1
                if(end < len(s)-1):
                    backward[end+1] -= 1
        
        ans = ''
        
        for i in range(1, len(s)):
            backward[i] += backward[i-1]
            forward[i] += forward[i-1]

        # print(forward, backward)
        for i in range(len(s)):
            offset = forward[i] - backward[i]
            ans += chr((ord(s[i]) - ord('a') + offset) % 26 + ord('a'))
        
        return ans
