# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lastUniqueNode = None
        
        temp = head
        prev = None
        
        while(temp):
            
            if(prev and temp.val != prev.val):
                lastUniqueNode = prev
                
            while(prev and temp and temp.val == prev.val):
                temp = temp.next
            
                
            if(lastUniqueNode != prev):
                
                if(lastUniqueNode == None):
                    head = temp
                else:
                    # print(lastUniqueNode.val, prev.val, temp.val)
                    lastUniqueNode.next = temp
            
            if(temp == None):
                return head

            prev = temp
            temp = temp.next
        
        return head
        