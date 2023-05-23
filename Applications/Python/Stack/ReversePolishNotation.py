class Solution:    
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []        

        for token in tokens:            
            if token == '/':                
                s = numbers.pop()
                f = numbers.pop()
                numbers.append(int(f / s))
            elif token == '*':
                s = numbers.pop()
                f = numbers.pop()
                numbers.append(f * s)                
            elif token == '-':
                s = numbers.pop()
                f = numbers.pop()
                numbers.append(f - s)                
            elif token == '+':
                s = numbers.pop()
                f = numbers.pop()
                numbers.append(f + s)                
            else:                
                numbers.append(int(token))

        return numbers.pop()