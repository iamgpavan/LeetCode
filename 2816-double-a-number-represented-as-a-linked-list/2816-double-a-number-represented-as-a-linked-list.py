# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        # ans_stack = []
        
        temp = head
        
        while(temp):
            stack.append(temp)
            temp = temp.next
        
        sum = 0
        carry = 0
        ans_head = None
        
        while(len(stack)):
            sum = 2*stack.pop().val + carry
            carry = sum // 10
            sum %= 10
            
            new_node = ListNode(sum)
            new_node.next = ans_head
            ans_head = new_node
        
        if(carry):
            # ans_stack.append(ListNode(carry))
            new_node = ListNode(carry)
            new_node.next = ans_head
            ans_head = new_node
        
#         ans_head = ans_stack.pop()
#         temp = ans_head
        
#         while(len(ans_stack)):
#             temp.next = ans_stack.pop()
#             temp = temp.next
        
        
        
        return ans_head