# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head==None or head.next==None or k == 0):
            return head
        first = head
        n = 0
        
        tmp = head
        
        while(tmp):
            tmp = tmp.next
            n += 1
        if(k%n == 0):
            return head
        
        for _ in range(k%n):
            first = first.next
        
        second = ListNode(0, head)
        
        while(first):
            # print(first.val, second.val)
            second = second.next
            first = first.next
            
        ans = second.next
        second.next = None
        
        tmp = ans
        
        while(tmp and tmp.next):
            tmp = tmp.next
        
        tmp.next = head
        
        return ans
        
        
        