# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root == None):
            return []
        ans = []
        
        queue = deque()
        queue.append(root)
        
        while(len(queue) != 0):
            n = len(queue)
            level = []
            while(n > 0):
                node = queue.popleft()
                level.append(node.val)
                
                if(node.left):
                    queue.append(node.left)
                
                if(node.right):
                    queue.append(node.right)
                n -= 1
            ans.append(level)
        
        return ans