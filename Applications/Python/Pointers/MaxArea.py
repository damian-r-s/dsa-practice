def maxArea(self, height: List[int]) -> int:
    maxW = 0
    l = 0
    r = len(height) - 1

    while l < r:
        hl = height[l]
        hr = height[r]
        w = min(hl, hr) * (r - l)
        if w > maxW:
            maxW = w

        if hl < hr:
            l += 1
        else:
            r -= 1
    
    return maxW