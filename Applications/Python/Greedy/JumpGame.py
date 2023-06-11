# 55. Jump Game
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

class Solution:   
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key =  lambda row: row[0])

        result = 0
        prev = intervals[0][1]

        for s, e in intervals[1:]:
            if s >= prev:
                prev = e
            else:
                result += 1
                prev = min(prev, e)

        return result