# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        postorderTraversal, stack = [], [(root, False)]
        
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    postorderTraversal.append(node.val)
                else:  # postorder: left -> right -> root
                    #Because it's a stack, last element will be our first element
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    
        return postorderTraversal
        
