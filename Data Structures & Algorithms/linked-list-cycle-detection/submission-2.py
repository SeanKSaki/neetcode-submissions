# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next          # Moves 1 step at a time
            fast = fast.next.next     # Moves 2 steps at a time
            
            # If pointers meet, a cycle exists
            if slow == fast:
                return True
        return False

        