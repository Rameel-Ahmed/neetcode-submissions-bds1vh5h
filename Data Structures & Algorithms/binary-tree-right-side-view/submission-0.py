# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def bfs(root):
            if root is None:
                return []
            queue=deque([root])
            levels=[]
            while queue:
                level=[]
                for _ in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
                levels.append(level)
            return levels
        list_incoming=bfs(root)
        list1=[]

        for i in list_incoming:
            list1.append(i[-1])
        return list1



        