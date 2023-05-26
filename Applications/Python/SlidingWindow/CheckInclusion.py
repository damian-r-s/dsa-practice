def checkInclusion(self, s1: str, s2: str) -> bool:
    lenS1 = len(s1)
    lenS2 = len(s2)

    if lenS1 > lenS2:
        return False

    frqS1 = [0]*26
    frqS2 = [0]*26

    for i in range(lenS1):
        frqS1[ord(s1[i]) - ord('a')] += 1
        frqS2[ord(s2[i]) - ord('a')] += 1

    for i in range(lenS2 - lenS1):            
        if frqS1 == frqS2:
            return True

        frqS2[ord(s2[i]) - ord('a')] -= 1
        frqS2[ord(s2[i + lenS1]) - ord('a')] += 1

    return frqS1 == frqS2