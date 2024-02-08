# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while(b!=0):
                a,b = b, a%b
            
            return a
        
        temp = head
        
        while(temp and temp.next):
            a = temp.val
            b = temp.next.val
            
            newNode = ListNode(gcd(a, b))
            newNode.next = temp.next
            temp.next = newNode
            temp = temp.next.next
        
        
        return head