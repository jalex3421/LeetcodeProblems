# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#preorder traversal: root, left, right --> this is the order to call the things...

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        preorderTraversal = []
        stack = [root]        
        
        while stack:
            #pop extract last element from list --> in this case left element
            node = stack.pop()
            if node:
                preorderTraversal.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
                
        return preorderTraversal 
    
