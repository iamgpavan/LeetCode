# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hm = {0 : None}
        
        prev = ListNode(0,head)
        curr = head
        curr_sum = 0
        
        while(curr):
            curr_sum += curr.val
            # print(curr.val, prev.val, curr_sum)
            if(curr_sum in hm):
                node = hm.get(curr_sum, None)
                # print(curr.val, node.val)
                
                tmp_curr = curr_sum
                
                if(node):
                    tmp = node.next
                else:
                    tmp = head
                while(tmp != curr):
                    tmp_curr += tmp.val
                    # print(hm, tmp_curr)
                    del hm[tmp_curr]
                    tmp = tmp.next
                
                if(node == None):
                    head = curr.next
                else:
                    node.next = curr.next
            else:
                hm[curr_sum] = curr
            
            prev = curr
            curr = curr.next
            
        
        return head