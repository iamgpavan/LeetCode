class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {"}" : "{", ')':'(', ']':'['}
        
        for i in s:
            if(i in hm):
                if (len(stack) and stack[-1] == hm[i]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if(len(stack)):
            return False
        
        return True