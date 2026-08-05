# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Use a list to store the maximum diameter found so far (mutable in nested function)
        res = [0]

        # DFS returns the maximum depth (in edges) from the current node down to a leaf
        def dfs(node):
            # Base case: empty node contributes -1 so that leaf nodes have depth 0
            if not node:
                return -1

            # Recursively get depths of left and right subtrees
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # The longest path passing through this node equals left_depth + right_depth + 2
            # (one edge to left child and one edge to right child)
            candidate = 2 + left_depth + right_depth
            res[0] = max(res[0], candidate)

            # Return the depth of this subtree to the parent
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return res[0]