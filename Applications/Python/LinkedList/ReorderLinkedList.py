# 143. Reorder List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        result = head.next
        lst = []

        while(result != None):
            lst.append(result)
            result = result.next


        l = 0
        r = len(lst) - 1
        result = head
        while (l <= r):
            result.next = lst[r]
            result.next.next = lst[l]
            result = result.next.next

            r -= 1
            l += 1

        result.next = None
