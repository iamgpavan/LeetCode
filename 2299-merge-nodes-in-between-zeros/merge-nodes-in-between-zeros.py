# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = ListNode(0)
        tempHead = ansHead
        
        temp = head
        curr_sum = 0
        
        while(temp and temp.val != 0):
            temp = temp.next
            
        temp = temp.next
        
        while(temp):
            if(temp.val == 0):
                newNode = ListNode(curr_sum)
                tempHead.next = newNode
                tempHead = tempHead.next
                curr_sum = 0
                    
            curr_sum += temp.val     
            temp = temp.next
        
        return ansHead.next
            