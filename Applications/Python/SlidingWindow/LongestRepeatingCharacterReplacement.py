# 424. Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

def characterReplacement(self, s: str, k: int) -> int:
    length = 0
    l = 0
    hm = {}
    frq = 0

    for r in range(len(s)):
        hm[s[r]] = 1 + hm.get(s[r], 0)
        frq = max(frq, hm[s[r]])

        if (r - l + 1) - frq > k:
            hm[s[l]] -= 1
            l += 1

        length = max(length, r - l + 1)
    
    return length