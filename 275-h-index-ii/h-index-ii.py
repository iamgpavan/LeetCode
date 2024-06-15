class Solution:
    def countUpperBound(self, n, arr, key):
        low = 0
        high = n-1
        
        while(low <= high):
            mid = (low + high)//2
            
            if(arr[mid] >= key):
                high = mid - 1
            else:
                low = mid + 1
        
        # print("high", high)
        return n - (high + 1) 
                
    def hIndex(self, citations: List[int]) -> int:
    
        n = len(citations)
        low = 0
        high = n
        ans = 0
        
        while(low <= high):
            mid = (low + high) // 2
            countGreater = self.countUpperBound(n, citations, mid)
            # print(" ---- ", countGreater, mid)
            if(countGreater == mid):
                ans = mid
                low = mid + 1
            elif(countGreater > mid):
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1
        
        # if(ans == 0):
        #     return n - high
        
        return ans