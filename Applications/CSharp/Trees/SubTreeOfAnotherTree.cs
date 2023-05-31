// 572. Subtree of Another Tree
// Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
// A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

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
    public bool IsSameTree(TreeNode p, TreeNode q)
    {
        if (p == null && q == null)
            return true;

        if (p != null && q != null && p.val == q.val)
            return IsSameTree(p.left, q.left) && IsSameTree(p.right, q.right);

        return false;
    }

    public bool IsSubtree(TreeNode root, TreeNode subRoot)
    {
        if (root == null)
            return false;

        if (IsSameTree(root, subRoot))
            return true;

        return IsSubtree(root.left, subRoot) || IsSubtree(root.right, subRoot);
    }
}

