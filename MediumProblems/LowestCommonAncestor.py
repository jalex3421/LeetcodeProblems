# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #1)Check wheter root is bigger than the other values --> check left subtree
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        #2)Check wheter root is smaller than the other values --> check right subtree
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        #Final condition: return root val
        return root
