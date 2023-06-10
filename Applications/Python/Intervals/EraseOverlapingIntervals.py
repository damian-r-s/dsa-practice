# 435. Non-overlapping Intervals
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

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