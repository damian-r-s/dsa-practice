from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for str in strs:            
            number = hash(''.join(sorted(str)))
            dic[number].append(str)
        
        return list(dic.values())