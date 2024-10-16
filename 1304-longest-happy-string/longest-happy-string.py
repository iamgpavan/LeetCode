import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        
        heapq.heapify(heap)
        
        ans = '  '
        
        
        
        while(len(heap)):
            firstpop = heapq.heappop(heap)
            
            if(firstpop[0] == 0):
                break
            
            if(firstpop[1] != ans[-1] or firstpop[1] != ans[-2]):
                ans += firstpop[1]
                heapq.heappush(heap, [firstpop[0]+1, firstpop[1]])
            else:
                secodnpop = heapq.heappop(heap)
                if(secodnpop[0] == 0):
                    break
                ans += secodnpop[1]
                heapq.heappush(heap, firstpop)
                heapq.heappush(heap, [secodnpop[0]+1, secodnpop[1]])

            # print(heap, ans)
        
        return ans[2:]
                