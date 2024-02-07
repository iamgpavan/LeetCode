# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        head = ListNode(0)
        temp = head
        
        numA = l1
        numB = l2
        sum = 0
        carry = 0
        
        while(numA and numB):
            sum = numA.val + numB.val + carry
            carry = sum // 10
            sum %= 10
            
            temp.next = ListNode(sum)
            temp = temp.next
            
            numA = numA.next
            numB = numB.next
        
        while(numA):
            sum = numA.val + carry
            carry = sum // 10
            sum %= 10
            
            temp.next = ListNode(sum)
            temp = temp.next
            
            numA = numA.next
        
        while(numB):
            sum = numB.val + carry
            carry = sum // 10
            sum %= 10
            
            temp.next = ListNode(sum)
            temp = temp.next
            
            numB = numB.next
        
        if(carry):
            temp.next = ListNode(carry)
        
        head = head.next
        
        return head