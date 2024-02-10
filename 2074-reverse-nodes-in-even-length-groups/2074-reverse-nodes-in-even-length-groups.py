# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node, length):
        temp = None
        curr_node = node
        
        while(length):
            temp2 = curr_node.next
            curr_node.next = temp
            temp = curr_node
            
            curr_node = temp2
            length -= 1
        
        return temp
        
        
    
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        length = 2
        prev = head
        curr = head.next
        actual_prev = head
        
        while(curr):
            curr_length = 0
            curr_head = curr
            
            while(curr and curr_length != length):
                actual_prev = curr
                curr = curr.next
                curr_length += 1
            
            
            if(curr_length % 2 == 0):
                prev.next = self.reverse(curr_head, curr_length)
                prev = curr_head
                prev.next = curr
            else:
                prev = actual_prev
            
            length += 1
        
        return head
        