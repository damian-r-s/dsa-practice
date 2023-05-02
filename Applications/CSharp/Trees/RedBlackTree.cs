class RedBlackTree
{
    private Node Root { get; private set; }
    class Node
    {
        public int Data { get; private set; }
        public Node Left { get; private set; }
        public Node Right { get; private set; }
        public Node Parent { get; private set; }
        //Red - false, Black - true
        public bool Colour { get; private set; }

        public Node(int data)
        {
            Data = data;
            Colour = false;
        }
    }

    private Node RotateRight(Node node)
    {
        Node x = node.Left;
        Node y = x.Right;
        x.Right = node;
        node.Left = y;
        node.Parent = x;

        if (y != null)
            y.Parent = node;

        return x;
    }

    private Node RotateLeft(Node node)
    {
        Node x = node.Right;
        Node y = x.Left;
        x.Left = node;
        node.Right = y;
        node.Parent = x;
        if (y != null)
            y.Parent = node;
        return x;
    }

    public void Insert(int data)
    {
        if (Root == null)
        {
            Root = new Node(data);
            Root.Colour = true;
        }
        else
        {
            Root = InsertHelp(Root, data);
        }
    }

    private bool ll = false;
    private bool rr = false;
    private bool lr = false;
    private bool rl = false;

    Node InsertHelp(Node root, int data)
    {
        var redRedConflict = false;

        if (root == null)
        {
            return new Node(data);
        }
        else if (data < root.Data)
        {
            root.Left = InsertHelp(root.Left, data);
            root.Left.Parent = root;
            if (root != Root)
            {
                if (root.Colour == false && root.Left.Colour == false)
                {
                    redRedConflict = true;
                }
            }
        }
        else
        {
            root.Right = InsertHelp(root.Right, data);
            root.Right.Parent = root;
            if (root != Root)
            {
                if (root.Colour == false && root.Right.Colour == false)
                {
                    redRedConflict = true;
                }
            }
        }

        if (ll)
        {
            root = RotateLeft(root);
            root.Colour = true;
            root.Left.Colour = false;
            ll = false;
        }
        else if (rr)
        {
            root = RotateRight(root);
            root.Colour = true;
            root.Right.Colour = false;
            rr = false;
        }
        else if (rl)
        {
            root.Right = RotateRight(root.Right);
            root.Right.Parent = root;
            root = RotateLeft(root);
            root.Colour = true;
            root.Left.Colour = false;
            rl = false;
        }
        else if (lr)
        {
            root.Left = RotateLeft(root.Left);
            root.Left.Parent = root;
            root.Colour = true;
            root.Right.Colour = false;
            lr = false;
        }

        if (redRedConflict)
        {
            if (root.Parent.Right == root) // to check which child is the current node of its parent
            {
                if (root.Parent.Left == null || root.Parent.Left.Colour == true) // case when parent's sibling is black
                {// perform certaing rotation and recolouring. This will be done while backtracking. Hence setting up respective flags.
                    if (root.Left != null && root.Left.Colour == false)
                        rl = true;
                    else if (root.Right != null && root.Right.Colour == false)
                        ll = true;
                }
                else // case when parent's sibling is red
                {
                    root.Parent.Left.Colour = true;
                    root.Colour = true;
                    if (root.Parent != this.Root)
                        root.Parent.Colour = false;
                }
            }
            else
            {
                if (root.Parent.Right == null || root.Parent.Right.Colour == true)
                {
                    if (root.Left != null && root.Left.Colour == false)
                        rr = true;
                    else if (root.Right != null && root.Right.Colour == false)
                        lr = true;
                }
                else
                {
                    root.Parent.Right.Colour = true;
                    root.Colour = true;
                    if (root.Parent != this.Root)
                        root.Parent.Colour = false;
                }
            }
            redRedConflict = false;
        }
    }
}