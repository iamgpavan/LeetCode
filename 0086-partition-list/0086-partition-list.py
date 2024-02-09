# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if(head == None):
            return head
        less_list_head = ListNode(0)
        great_list_head = ListNode(0)
        
        less_list_temp = less_list_head
        great_list_temp = great_list_head
        
        temp = head
        
        while(temp):
            if(temp.val < x):
                less_list_temp.next = temp
                less_list_temp = less_list_temp.next
                
            else:
                # print(temp.val)
                great_list_temp.next = temp
                great_list_temp = great_list_temp.next
                
            
            temp = temp.next
        
        great_list_temp.next = None
        
        # if(less_list_head.next == None):
        #     return great_list_head.next
        
        less_list_temp.next = great_list_head.next
        
        return less_list_head.next