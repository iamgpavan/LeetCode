# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node, diameter):
            if(not node):
                return 0
            
            left = height(node.left, diameter)
            right = height(node.right, diameter)
            diameter[0] = max(diameter[0], left+right)

            return 1 + max(left, right)
        diameter = [0]
        height(root, diameter)
        return diameter[0]