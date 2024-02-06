# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        prev = None
        
        while(temp):
            while(temp and temp.val == val):
                if(prev == None):
                    head = temp.next
                else:
                    prev.next = temp.next
                
                temp = temp.next
            
            if(temp == None):
                return head
            
            prev = temp
            temp = temp.next
        
        return head