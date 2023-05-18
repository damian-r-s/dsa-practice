
public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution
{
    TreeNode next;
    public TreeNode IncreasingBST(TreeNode root)
    {
        if (root == null)
        {
            return null;
        }
        var beginning = next = new TreeNode();

        InOrder(root);
        return beginning.right;
    }

    private void InOrder(TreeNode node)
    {
        if (node == null)
            return;

        InOrder(node.left);
        node.left = null;
        next.right = node;
        next = node;
        InOrder(node.right);
    }
}