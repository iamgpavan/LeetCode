class Solution:
    def validStrings(self, n: int) -> List[str]:
        def helper(curr, zero):
            if(len(curr) == n):
                self.ans.append(curr)
                return 
            
            if(zero == 1):
                helper(curr + "1", 0)
            else:
                helper(curr + "0", 1)
                helper(curr + "1", 0)
            
        self.ans = []
        
        helper("0", 1)
        helper("1", 0)
        
        return self.ans
            