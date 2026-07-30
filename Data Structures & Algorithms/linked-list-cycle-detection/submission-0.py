# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head # two pointers start at head

        while fast and fast.next:   # while fast can move two steps
            slow = slow.next  # slow moves one step
            fast = fast.next.next  # fast moves two steps
            if slow == fast: # if pointers meet then cycle detected
                return True

        return False               