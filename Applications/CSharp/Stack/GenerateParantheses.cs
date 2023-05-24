class Solution {
    public IList<string> GenerateParenthesis(int n) {
        var result = new List<string>();
        var stack = new Stack<char>();

        void Rec(int c, int o)
        {
            if(c == n && o == n)
            {                
                 result.Add(new string(stack.Reverse().ToArray()));
            }

            if (c < n)
            {
                stack.Push('(');
                Rec(c + 1, o);
                stack.Pop();
            }

            if(o < c)
            {
                stack.Push(')');
                Rec(c, o + 1);
                stack.Pop();
            }
        }

        Rec(0, 0);
        return result;   
    }
}