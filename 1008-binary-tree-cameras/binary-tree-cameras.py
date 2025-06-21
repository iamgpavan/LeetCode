# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # if(root.right is None and root.left is None):
        #     return 1
        def camera(node, ans):
            if(not node):
                return 1
            
            left = camera(node.left, ans)
            right = camera(node.right, ans)

            if(left == 0 or right == 0):
                ans[0] += 1
                return 2
            elif(left == 2 or right == 2):
                return 1
            return 0
        
        ans = [0]
        if camera(root, ans) == 0:
            ans[0] += 1
        return ans[0]
