// 230. Kth Smallest Element in a BST
// Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

class TreeNode
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

class Solution
{
    private List<int> values = new List<int>();
    private static int counter = 0;

    public int KthSmallest(TreeNode root, int k)
    {
        counter = k;
        return Rec(root);
    }

    private int Rec(TreeNode root)
    {
        if (root == null)
            return -1;

        var left = Rec(root.left);
        if (left != -1)
            return left;

        counter--;
        if (counter == 0)
            return root.val;

        var right = Rec(root.right);
        if (right != -1)
            return right;

        return -1;
    }
}