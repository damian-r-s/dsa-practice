class Solution
{
    public int EvalRPN(string[] tokens)
    {
        Stack<int> stack = new Stack<int>();

        foreach (string token in tokens)
        {
            if (IsNumeric(token))
            {
                stack.Push(int.Parse(token));
            }
            else
            {
                int op2 = stack.Pop();
                int op1 = stack.Pop();
                int result = PerformOperation(token, op1, op2);
                stack.Push(result);
            }
        }

        return stack.Pop();
    }

    private bool IsNumeric(string token)
    {
        return int.TryParse(token, out _);
    }

    private int PerformOperation(string token, int operand1, int operand2)
    {
        switch (token)
        {
            case "+":
                return operand1 + operand2;
            case "-":
                return operand1 - operand2;
            case "*":
                return operand1 * operand2;
            case "/":
                return operand1 / operand2;
            default:
                throw new ArgumentException("Invalid operator: " + token);
        }
    }
}
