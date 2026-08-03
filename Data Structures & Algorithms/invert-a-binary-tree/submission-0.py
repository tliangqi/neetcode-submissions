# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if current node is None, return None
        if not root:
            return None

        # Swap the left and right children of the current node
        tmp = root.left          # temporarily store the left child
        root.left = root.right   # set left child to the original right child
        root.right = tmp         # set right child to the original left child

        # Recursively invert the left subtree (now it's the original right subtree)
        self.invertTree(root.left)
        # Recursively invert the right subtree (now it's the original left subtree)
        self.invertTree(root.right)

        # Return the root of the inverted tree
        return root