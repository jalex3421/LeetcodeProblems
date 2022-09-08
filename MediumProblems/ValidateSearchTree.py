 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #lessThan --> all the nodes smaller than this one
    #largerThan --> all the nodes bigger than this one
    def isValidBST(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        #is given BST is empty
        if not root:
            return True
        #if root don't follow any normal requisite
        if (root.val <= largerThan) or (root.val >= lessThan):
            return False
        #recursive call--> udpate lessThan and largerThan
        return self.isValidBST(root.left, min(lessThan, root.val), largerThan) and self.isValidBST(root.right, lessThan, max(root.val, largerThan))
