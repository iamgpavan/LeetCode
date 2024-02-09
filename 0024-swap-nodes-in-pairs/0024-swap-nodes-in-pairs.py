# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        
        curr = head
        prev = None
        
        while(curr and curr.next):
            temp = curr.next
            curr.next = temp.next
            if(prev == None):
                head = temp
            else:
                prev.next = temp
            temp.next = curr
            
            prev = curr            
            curr = curr.next
        
        return head
            
            