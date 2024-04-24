class Solution:
    def tribonacci(self, n: int) -> int:
        if(n == 0):
            return 0
        if(n<=2):
            return 1
        t_n_2 = 0
        t_n_1 = 1
        t_n = 1
        
        while(n-2 > 0):
            tmp = t_n
            t_n += t_n_1 + t_n_2
            t_n_2 = t_n_1
            t_n_1 = tmp
            
            n -= 1
        
        return t_n