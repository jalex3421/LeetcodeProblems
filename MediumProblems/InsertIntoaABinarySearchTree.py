# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Insert element in BST, and return new tree generated. The val is GUARANTEED TO NOT EXIST IN THE 
# TREE!!

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #Option 1: BST is empty --> new three node
        if (root == None):
            return TreeNode(val)
        #Second option --> check right subtree
        elif (val > root.val):
            root.right = self.insertIntoBST(root.right,val)
        #Third option --> check left subtree
        elif (val < root.val):
            root.left = self.insertIntoBST(root.left,val)
        #root is not None and
        return root
        
