/**
 * Definition for a binary tree node.

 */

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int rangeSumBST(struct TreeNode *root, int low, int high)
{
    if (root == 0)
    {
        return 0;
    }

    int sum = 0;
    if (root->val > low)
    {
        sum += rangeSumBST(root->left, low, high);
    }
    if (low <= root->val && root->val <= high)
    {
        sum += root->val;
    }
    if (root->val < high)
    {
        sum += rangeSumBST(root->right, low, high);
    }

    return sum;
}

int main(void)
{
    return 0;
}