# 20. Valid Parentheses
# Solved
# Easy
# Topics
# premium lock iconCompanies
# Hint

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            c = s[i]

            if c == '(' or c == '{' or  c=='[':
                stack.append(c)
            else:   
                if not stack:
                    return False
                    
                prev = stack.pop()

                if c == '}' and prev == '{':
                    continue
                if c == ')' and prev == '(':
                    continue
                if c == ']' and prev == '[':
                    continue
                
                return False

        return len(stack) == 0