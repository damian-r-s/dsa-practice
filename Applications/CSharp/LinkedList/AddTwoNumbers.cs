// 2. Add Two Numbers
// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
}

class Solution
{
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    {
        ListNode head = new ListNode(0);
        var curr = head;
        var acu = 0;

        while (l1 != null || l2 != null)
        {
            var v1 = l1 == null ? 0 : l1.val;
            var v2 = l2 == null ? 0 : l2.val;
            var sum = acu + v1 + v2;
            acu = sum / 10;
            sum = sum % 10;

            curr.next = new ListNode(sum);
            curr = curr.next;

            l1 = l1 == null ? null : l1.next;
            l2 = l2 == null ? null : l2.next;
        }

        if (acu != 0)
        {
            curr.next = new ListNode(acu);
        }

        return head.next;
    }
}