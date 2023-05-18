/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode *next;

struct TreeNode *increasingBST(struct TreeNode *root)
{
    if (root == 0)
        return 0;

    struct TreeNode *beginning = next = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    inOrder(root);
    return beginning->right;
}

void inOrder(struct TreeNode *node)
{
    if (node == 0)
    {
        return 0;
    }

    inOrder(node->left);
    node->left = 0;
    next->right = node;
    next = node;
    inOrder(node->right);
}