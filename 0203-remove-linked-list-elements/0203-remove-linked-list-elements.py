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
            flag = False
            while(temp and temp.val == val):
                flag = True    
                temp = temp.next
            
            if(flag):
                if(prev == None):
                    head = temp
                else:
                    prev.next = temp
            
            if(temp == None):
                return head
            
            prev = temp
            temp = temp.next
        
        return head