class MinStack
{
    private Stack<int> stack = new Stack<int>();
    private Stack<int> minStack = new Stack<int>();

    public MinStack()
    {

    }

    public void Push(int x)
    {
        stack.Push(x);

        if (minStack.Count == 0 || x <= minStack.Peek())
            minStack.Push(x);
    }

    public void Pop()
    {
        int popped = stack.Pop();

        if (popped == minStack.Peek())
            minStack.Pop();
    }

    public int Top()
    {
        return stack.Peek();
    }

    public int GetMin()
    {
        return minStack.Peek();
    }
}