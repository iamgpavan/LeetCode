# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        
        while(temp):
            dummy = temp.next
            
            while(dummy and dummy.val == temp.val):
                dummy = dummy.next
            
            if(dummy != temp.next):
                temp.next = dummy
            
            temp = temp.next
            
            
        return head