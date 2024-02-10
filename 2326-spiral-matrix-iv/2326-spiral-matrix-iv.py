# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1 for i in range(n)] for j in range(m)]
        
        temp = head
        i = 0
        j = 0
        direction = 1
        
        while(temp):
            ans[i][j] = temp.val
            temp = temp.next
            
            if(direction == 1):
                j += 1
                
                if(j == n or ans[i][j] != -1):
                    direction = 2
                    i += 1
                    j -= 1
                    
            elif(direction == 2):
                i += 1
                
                if(i == m or ans[i][j] != -1):
                    direction = 3
                    i -= 1
                    j -= 1
            elif(direction == 3):
                j -= 1
                
                if(j < 0 or ans[i][j] != -1):
                    direction = 4
                    j += 1
                    i -= 1
            elif(direction == 4):
                i -= 1
                
                if(i < 0 or ans[i][j] != -1):
                    direction = 1
                    i += 1
                    j += 1
            
        
        return ans