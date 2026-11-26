# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        list1=[]
        def inorder(root):
            nonlocal list1
            if root is None:
                return
            inorder(root.left)
            list1.append(root.val)
            inorder(root.right)
        inorder(root)
        minimum= float("inf")
        for i in range(len(list1)-1):
            cal = list1[i+1]-list1[i]
            if cal<minimum:
                minimum = cal
        return minimum 
            
        