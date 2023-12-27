class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:        
        ans = 0
        prev = neededTime[0]
        
        for i in range(1, len(colors)):
            if(colors[i] == colors[i-1]):
                ans += min(neededTime[i], prev)
                prev = max(prev, neededTime[i])
            else:
                prev = neededTime[i]
                   
        return ans