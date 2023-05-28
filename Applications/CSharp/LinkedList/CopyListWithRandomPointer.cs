// 138. Copy List with Random Pointer

class Node
{
    public int val;
    public Node next;
    public Node random;

    public Node(int _val)
    {
        val = _val;
        next = null;
        random = null;
    }
}

class Solution
{
    public Node CopyRandomList(Node head)
    {
        if (head == null)
            return null;

        var map = new Dictionary<int, Node>();

        var curr = head;
        while (curr != null)
        {
            var cp = new Node(curr.val);
            map.Add(curr.GetHashCode(), cp);
            curr = curr.next;
        }

        curr = head;
        while (curr != null)
        {
            var cp = map[curr.GetHashCode()];
            if (curr.next != null)
                cp.next = map[curr.next.GetHashCode()];
            if (curr.random != null)
                cp.random = map[curr.random.GetHashCode()];
            curr = curr.next;
        }

        return map[head.GetHashCode()];
    }
}