# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack = []
        l2_stack = []
        
        l1_temp = l1
        l2_temp = l2
        
        while(l1_temp):
            l1_stack.append(l1_temp)
            l1_temp = l1_temp.next
        
        while(l2_temp):
            l2_stack.append(l2_temp)
            l2_temp = l2_temp.next
            
        carry = 0
        temp = None        
        
        while(len(l1_stack) and len(l2_stack)):
            a = l1_stack.pop().val
            b = l2_stack.pop().val
            
            sum = a + b + carry
            carry = sum // 10
            sum %= 10
            
            newNode = ListNode(sum)
            newNode.next = temp
            temp = newNode
        
        while(len(l1_stack)):
            a = l1_stack.pop().val
            
            sum = a + carry
            carry = sum // 10
            sum %= 10
            
            newNode = ListNode(sum)
            newNode.next = temp
            temp = newNode
        
        while(len(l2_stack)):
            b = l2_stack.pop().val
            
            sum = b + carry
            carry = sum // 10
            sum %= 10
            
            newNode = ListNode(sum)
            newNode.next = temp
            temp = newNode
        
        if(carry):
            newNode = ListNode(carry)
            newNode.next = temp
            temp = newNode
        
        head = temp
        return head