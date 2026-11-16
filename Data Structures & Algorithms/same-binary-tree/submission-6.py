# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root, subRoot):
        def same(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a.val != b.val:
                return False
            return same(a.left, b.left) and same(a.right, b.right)

        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if same(root, subRoot):
            return True
        return (self.isSameTree(root.left, subRoot) or
                self.isSameTree(root.right, subRoot))