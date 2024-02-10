"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(head == None):
            return head
        
        # Adding new node to next of every node in original list
        temp = head
        
        while(temp):
            newNode = Node(temp.val, temp.next)
            # newNode.next = temp.next
            temp.next = newNode
            temp = temp.next.next
            
        # temp_random = head.random
        
        temp = head
        
        # Attaching random nodes of copied node
        while(temp):
            temp_random = temp.random
            if(temp_random):
                temp.next.random = temp_random.next
            
            temp = temp.next.next
        
        # Detaching copied node from original list
        ans = head.next
        ref = ans
        
        temp = head
        
        while(ref.next):
            temp.next = temp.next.next
            temp = temp.next
            
            ref.next = ref.next.next
            ref = ref.next
        
        return ans