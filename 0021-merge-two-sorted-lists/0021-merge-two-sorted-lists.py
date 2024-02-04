# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None):
            return list2
        if(list2 == None):
            return list1
        
        head = None
        temp1 = list1
        temp2 = list2
        
        if(list1.val < list2.val):
            head = list1
            temp1 = temp1.next
        else:
            head = list2
            temp2 = temp2.next
        
        tempHead = head
        
        while(temp1 and temp2):
            if(temp1.val < temp2.val):
                tempHead.next = temp1
                tempHead = tempHead.next
                temp1 = temp1.next
            else:
                tempHead.next = temp2
                tempHead = tempHead.next
                temp2 = temp2.next
        
        if(temp1):
            tempHead.next = temp1
        
        if(temp2):
            tempHead.next = temp2
        
        return head
            