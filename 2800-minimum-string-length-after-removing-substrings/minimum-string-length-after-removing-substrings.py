class Solution:
    def minLength(self, s: str) -> int:
        stack = [s[0]]
        
        i = 1
        
        while(i < len(s)):
            # print(stack)
            if(s[i] == "B"):
                if(len(stack) and stack[-1] == 'A'):
                    stack.pop()
                else:
                    stack.append(s[i])
            elif(s[i] == "D"):
                if(len(stack) and stack[-1] == "C"):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
                        
            i += 1
        
        return len(stack)