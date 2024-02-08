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
        start = False
        curr_sum = 0
        
        while(temp):
            # print(temp.val, start, curr_sum)
            if(temp.val == 0):
                if(start):
                    newNode = ListNode(curr_sum)
                    tempHead.next = newNode
                    tempHead = tempHead.next
                    curr_sum = 0
                else:
                    start = True
                    
            curr_sum += temp.val     
            temp = temp.next
        
        return ansHead.next
            