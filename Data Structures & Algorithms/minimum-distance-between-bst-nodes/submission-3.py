# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = None
        minimum = float('inf')
        def inorder(root):
            nonlocal prev,minimum
            if root is None:
                return
            inorder(root.left)
            if prev is not None:
                minimum = min(minimum, root.val - prev)
            prev = root.val
            inorder(root.right)
        inorder(root)
        return minimum