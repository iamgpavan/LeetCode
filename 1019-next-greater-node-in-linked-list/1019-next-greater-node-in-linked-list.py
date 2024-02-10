# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        
        curr = head
        ans = []
        ind = 0
        
        while(curr):
            value = curr.val
            ans.append(0)
            
            # print( value, stack)
            while(len(stack) and value > stack[-1][0]):    
                dm, dind = stack.pop()
                
                ans[dind] = value
                
            stack.append([value, ind])
            ind += 1
            curr = curr.next
        
        return ans