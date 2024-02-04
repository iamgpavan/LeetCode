# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA
        tempB = headB
        flagA = False
        flagB = False
        
        while(tempA and tempB):
            # print(tempA.val, tempB.val)
            if(tempA == tempB):
                return tempA
            
            tempA = tempA.next
            tempB = tempB.next
            
            if(tempA == None):
                if(flagA):
                    return None
                flagA = True
                tempA = headB
            
            if(tempB == None):
                if(flagB):
                    return None
                flagB = True
                tempB = headA
        
        return None 
            