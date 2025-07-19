package Applications.Java.LinkedList;

import java.util.ArrayList;

class ListNode{
    int val;
    ListNode next;

    ListNode(int val)
    {
        this.val = val;
    }
}

public class MiddleOfTheLinkedList {
    public static ListNode middleNode(ListNode head) 
    {
        ListNode middle = head;
        ListNode end = head;

        while(end != null && end.next != null)        
        {
            middle = middle.next;
            end = end.next.next;
        }

        return middle;
    }
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        ListNode middle = middleNode(head);

        System.out.println("Middle node value: " + middle.val); // Should print 3      
    }
}
