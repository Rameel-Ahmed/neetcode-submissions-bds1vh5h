# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        has_seen = {}
        current = head
        while current:
            has_seen[current]=0
            current = current.next
            if current in has_seen:
                return True
        return False 
        