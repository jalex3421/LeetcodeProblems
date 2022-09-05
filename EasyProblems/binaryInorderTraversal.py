# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Inorder: left-root-right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorderTraversal, stack = [], [(root, False)]
        
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    inorderTraversal.append(node.val)
                else:  # inorder: left -> root -> right
                    #Because it's a stack, last element will be our first element
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return inorderTraversal
    
