# 138. Copy List with Random Pointer


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        copies = {None: None}

        curr = head
        while curr:
            cp = Node(curr.val)
            copies[curr] = cp
            curr = curr.next

        curr = head
        while curr:
            cp = copies[curr]
            cp.next = copies[curr.next]
            cp.random = copies[curr.random]
            curr = curr.next

        return copies[head]