# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify edge cases (empty list handling)
        dummy = ListNode()
        cur = dummy          # Pointer to the current tail of the result list

        carry = 0            # Carry-in from the lower digit (0 or 1)

        # Loop while either list has nodes left or there is a remaining carry
        while l1 or l2 or carry:
            # Get current values; if node is None, treat it as 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Sum of current digits plus carry
            total = v1 + v2 + carry
            carry = total // 10       # Compute new carry for the next higher digit
            digit = total % 10        # Current digit of the result

            # Append the new digit as a node to the result list
            cur.next = ListNode(digit)
            cur = cur.next            # Move the tail pointer forward

            # Advance l1 and l2 to their next nodes (or None if exhausted)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the real head of the result list (skip the dummy node)
        return dummy.next