class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        
        i = len(a)-1
        j = len(b)-1
        
        curr_sum = 0
        carry = 0
        
        while(i>=0 and j>=0):
            x = int(a[i])
            y = int(b[j])
            curr_sum = x+y+carry
            carry = curr_sum//2
            curr_sum %= 2
            ans += str(curr_sum)
            i-=1
            j-=1
        
        while(i>=0):
            x = int(a[i])
            curr_sum = x+carry
            carry = curr_sum//2
            curr_sum %= 2
            ans += str(curr_sum)
            i-=1
        
        while(j>=0):
            y = int(b[j])
            curr_sum = y+carry
            carry = curr_sum//2
            curr_sum %= 2
            ans += str(curr_sum)
            j-=1
        
        if(carry):
            ans += str(carry)
        
        return ans[::-1]