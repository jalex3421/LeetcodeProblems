# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        return self.checkMirror(root.left,root.right)
    
    def checkMirror(self, left,right):
        #check if both elements are none
        if right is None and left is None:
            return True
        #check if only one element is none
        if right is None or left is None:
            return False
        #in the case both roots have the same val...
        if (left.val == right.val):
            return self.checkMirror(left.left,right.right) and self.checkMirror(left.right,right.left)
        else:
            return False
    
