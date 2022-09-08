# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, Targetsum):
        #if is empty the structure
        if not root: return False
        #if node.val is same as target
        if not root.left and not root.right and root.val == Targetsum: return True
        #update target sum
        Targetsum -= root.val
        return self.hasPathSum(root.left, Targetsum) or self.hasPathSum(root.right, Targetsum)
