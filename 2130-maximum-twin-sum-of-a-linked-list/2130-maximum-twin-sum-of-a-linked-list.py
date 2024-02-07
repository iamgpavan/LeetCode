# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        
        while(fast):
            fast = fast.next.next
            slow = slow.next
        
        half_stack = []
        
        # slow = slow.next
        
        while(slow):
            half_stack.append(slow)
            slow = slow.next
        
        temp = head
        max_so_far = 0
        
        while(len(half_stack)):
            node = half_stack.pop()
            max_so_far = max(max_so_far, temp.val+node.val)
            temp = temp.next
        
        return max_so_far