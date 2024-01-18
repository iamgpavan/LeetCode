class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<=2):
            return n
        
        one = 1
        two = 2
        i = 2
        while(i<n):
            temp = two
            two = two+one
            one = temp
            
            i+=1
        
        return two