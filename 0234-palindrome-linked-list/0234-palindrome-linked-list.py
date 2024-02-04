# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find mid node
        fast = head
        slow = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        # Place mid node based on odd or even length
        midNode = slow
        
        if(fast):
            midNode = slow.next
        
        # Reverse second half
        curr = midNode
        prev = None
        
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Compare values
        firstHead = head
        lastHead = prev
        
        while(firstHead and lastHead):
            print(firstHead.val, lastHead.val)
            if(firstHead.val != lastHead.val):
                return False
            
            firstHead = firstHead.next
            lastHead = lastHead.next
        
#         if(firstHead):
#             print("here, first")
#             return False
        
#         if(secondHead):
#             print("here, last")
#             return False      
        
        
        return True
        
        