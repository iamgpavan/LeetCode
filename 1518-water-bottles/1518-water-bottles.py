class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        
        n = numBottles
        while(n >= numExchange):
            k = n //numExchange
            ans += k
            n = k + (n%numExchange)
        
        return ans