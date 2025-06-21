# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def robber(root):
            if(root == None):
                return 0, 0

            leftRob, leftNotRob = robber(root.left)
            rightRob, rightNotRob = robber(root.right)

            currentRob = root.val + leftNotRob + rightNotRob 
            currentNotRob = max(leftRob, leftNotRob) + max(rightRob, rightNotRob)

            return currentRob, currentNotRob
        
        return max(robber(root))