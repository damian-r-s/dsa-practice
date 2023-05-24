# 739. Daily Temperatures

def dailyTemperatures(self, temperatures):
    stack = []
    result = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            _ , idx = stack.pop()
            result[idx] = i - idx
        stack.append((t, i))

    return result