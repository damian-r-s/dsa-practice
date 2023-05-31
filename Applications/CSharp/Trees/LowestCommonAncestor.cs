// 235. Lowest Common Ancestor of a Binary Search Tree
// Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
// According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}


class Solution
{
    public TreeNode LowestCommonAncestorRec(TreeNode root, TreeNode p, TreeNode q)
    {
        if (p.val < root.val && q.val < root.val)
            return LowestCommonAncestor(root.left, p, q);
        else if (p.val > root.val && q.val > root.val)
            return LowestCommonAncestor(root.right, p, q);

        return root;
    }

    public TreeNode LowestCommonAncestorLoop(TreeNode root, TreeNode p, TreeNode q)
    {
        while (root != null)
        {
            if (root.val > p.val && root.val > q.val)
            {
                root = root.left;
            }
            else if (root.val < p.val && root.val < q.val)
            {
                root = root.right;
            }
            else
                break;
        }

        return root;
    }
}