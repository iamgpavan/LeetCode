# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if(head.next == None and head.next.next == None):
            return [-1, -1]
        
        prev = head
        curr = head.next
        forw = head.next.next
        
        min_dis = 10**6
        start_critcal_point = 0
        prev_critical_point = 0
        max_dis = -1
        curr_pos = 2
        
        while(forw):
            # print(prev.val, curr.val, forw.val, (prev.val < curr.val < forw.val), (prev.val > curr.val > forw.val))
            if(prev.val < curr.val > forw.val) or (prev.val > curr.val < forw.val):
                # print(curr_pos, start_critcal_point, prev_critical_point)
                if(start_critcal_point == 0) : 
                    start_critcal_point = curr_pos   
                else:
                    min_dis = min(min_dis, curr_pos - prev_critical_point)
                    max_dis = curr_pos - start_critcal_point        
                prev_critical_point = curr_pos
            
            curr_pos += 1
            prev = prev.next
            curr = curr.next
            forw = forw.next
        
        if(min_dis == 10**6):
            min_dis = -1
        
        
        return [min_dis, max_dis]       