// 199. Binary Tree Right Side View
// Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

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
    public IList<int> RightSideView(TreeNode root)
    {
        var res = new List<int>();
        if (root == null)
            return res;

        var q = new Queue<TreeNode>(new TreeNode[] { root });
        while (q.Count > 0)
        {
            var size = q.Count;
            TreeNode curr = null;
            for (int i = 0; i < size; i++)
            {
                curr = q.Dequeue();
                if (curr.left != null)
                    q.Enqueue(curr.left);

                if (curr.right != null)
                    q.Enqueue(curr.right);
            }
            res.Add(curr.val);
        }

        return res;
    }
}