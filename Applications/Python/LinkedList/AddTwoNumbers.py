# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        cur = head
        acu = 0
        
        while l1 or l2:
            v1 = 0
            if l1 is not None:
                v1 = l1.val
            v2 = 0
            if l2 is not None:
                v2 = l2.val

            sum = v1 + v2 + acu
            acu = sum // 10
            sum = sum % 10

            cur.next = ListNode(sum)
            cur = cur.next
            if l1 is None:
                l1 = None
            else:
                l1 = l1.next
            
            if l2 is None:
                l2 = None
            else:
                l2 = l2.next               


        if acu != 0:
            cur.next = ListNode(acu)

        return head.next