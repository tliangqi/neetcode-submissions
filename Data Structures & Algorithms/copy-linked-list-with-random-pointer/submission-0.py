"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        # First pass: create a copy for each original node
        cur = head
        while cur:
            copy = Node(cur.val)   # new node with same value
            oldToCopy[cur] = copy  # store mapping
            cur = cur.next

        # assign next and random pointers for the copied nodes
        cur = head
        while cur:
            copy = oldToCopy[cur]   # get the copy of current node
            copy.next = oldToCopy[cur.next]   # link next pointer
            copy.random = oldToCopy[cur.random]  # link random pointer
            cur = cur.next

        # Return the head of the newly copied list
        return oldToCopy[head]