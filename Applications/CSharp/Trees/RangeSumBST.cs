class RangeSumBST
{
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
    };

    static int RangeSum(TreeNode root, int low, int high)
    {
        if (root == null)
            return 0;

        int sum = 0;
        if (root.val > low)
        {
            sum += RangeSum(root.left, low, high);
        }

        if (low <= root.val && root.val <= high)
        {
            sum += root.val;
        }

        if (root.val < high)
        {
            sum += RangeSumBST(root.right, low, high);
        }
        return sum;
    }
}



