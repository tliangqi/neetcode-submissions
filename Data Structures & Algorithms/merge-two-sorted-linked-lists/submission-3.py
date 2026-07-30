# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # simplify head handling
        tail = dummy  # Tail pointer for merged list

        while list1 and list2:    # Compare nodes while both lists have elements
            if list1.val < list2.val:
                tail.next = list1 # Attach the smaller node
                list1 = list1.next  # Move l1 pointer forward
            else:
                tail.next = list2   
                list2 = list2.next    # Move l2 pointer forward
            tail = tail.next  # Advance tail to last node

        # Append the remaining nodes
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next  # Return the actual head of merged list