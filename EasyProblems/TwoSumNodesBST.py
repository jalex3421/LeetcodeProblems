# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        #iterative approach
        #initialize variables
        stack, seen = [root], set()
        #iterate
        while stack:
            curr = stack.pop()
            # If we've seen k - curr.val --> (curr.val) + k-curr.val 
            if k - curr.val in seen:
                return True
            seen.add(curr.val)
            # check children
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)     
        return False
    
