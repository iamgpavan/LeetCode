# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if(left == right):
            return head
        
        prev = ListNode(0, head)
        curr = head
        
        cnt = 1
        
        while(cnt != left and curr):
            prev = curr
            curr = curr.next
            
            cnt += 1
            
        
        tempCurr = None
        tempStart = curr
        temp = None
        
        while(cnt != right+1 and curr):
            # print(curr.val)
            temp = curr.next
            curr.next = tempCurr
            tempCurr = curr
            
            curr = temp
            cnt += 1
        # print(temp.val)
            
        tempStart.next = temp
        prev.next = tempCurr
        
        if(left == 1):
            return tempCurr
        
        return head