# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # Dummy node simplifies edge cases 
        left = dummy      # left points to predecessor of target
        right = head      # right will lead by n steps

        # Move right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Skip the target node (left.next is the nth from end)
        left.next = left.next.next

        # Return the new head (dummy.next)
        return dummy.next