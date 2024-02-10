# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        
        even_ptr = head.next        
        even_end_ptr = even_ptr
        if(even_end_ptr.next == None):
            return head
        
        odd_ptr = head
        odd_end_ptr = head
        
        flag = False
        
        
        curr = head
        
        while(curr):
            if(flag):
                # print()
                temp = even_end_ptr.next
                even_end_ptr.next = temp.next
                even_end_ptr = even_end_ptr.next
                odd_end_ptr.next = temp
                odd_end_ptr = odd_end_ptr.next
                flag = False 
            else:
                flag = True
                
            curr = curr.next
        
        odd_end_ptr.next = even_ptr
        
        return head
        