# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

class Solution:
    def letterCombinations(self, digits: str):
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def back(i, curStr):
            if len(digits) == i:
                res.append(curStr)
                return

            for c in dic[digits[i]]:
                back(i + 1, curStr + c)

        if digits:
            back(0, "")
            
        return res
        
