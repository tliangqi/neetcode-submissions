# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Edge case: empty tree has depth 0
        if not root:
            return 0
        
        # Stack stores each frame as [node, current_depth]
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            # Pop the top frame
            node, depth = stack.pop()
            
            # Update the maximum depth seen so far
            max_depth = max(max_depth, depth)
            
            # Push left and right children with depth+1 (if they exist)
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        
        return max_depth