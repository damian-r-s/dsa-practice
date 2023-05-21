bool IsValid(string s)
{
    var stack = new Stack<char>();

    Dictionary<char, char> bracketMap = new Dictionary<char, char>
    {
        { '(', ')' },
        { '{', '}' },
        { '[', ']' }
    };

    foreach (char c in s)
    {
        if (bracketMap.ContainsKey(c))
        {
            stack.Push(c);
        }
        else if (bracketMap.ContainsValue(c))
        {
            if (stack.Count == 0 || bracketMap[stack.Peek()] != c)
            {
                return false;
            }
            stack.Pop();
        }
    }

    return stack.Count == 0;
}