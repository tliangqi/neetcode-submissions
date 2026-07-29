# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # empty list or end of recursion.
        if not head:
            return None

        # Assume current head is the new head initially.
        newHead = head

        # If there is a next node, reverse the rest recursively.
        if head.next:
            newHead = self.reverseList(head.next) # Reverse the sublist 
            
            head.next.next = head  # Point the old tail back to current head.

            head.next = None # Break the original forward link to avoid cycle.

        return newHead