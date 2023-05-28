// 206. Reverse Linked List
// Given the head of a singly linked list, reverse the list, and return the reversed list.
// Definition for singly-linked list.

class ListNode
{
    public int val;
    public ListNode next;
    public ListNode(int val = 0, ListNode next = null)
    {
        this.val = val;
        this.next = next;
    }
};

class Solution
{
    ListNode ReverseList(ListNode head)
    {
        if (head == null || head.next == null)
        {
            return head;
        }

        var res = ReverseList(head.next);
        head.next.next = head;
        head.next = null;
        return res;
    }
}