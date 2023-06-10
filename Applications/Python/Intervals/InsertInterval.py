# 57. Insert Interval
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        combined = newInterval
        
        for i  in range(len(intervals)):
            current = intervals[i]
            if combined[1] < current[0]:
                result.append(combined)
                return result + intervals[i:]                
            elif combined[0] > current[1]:
                result.append(current)
            else:
                combined = [
                    min(combined[0], current[0]),
                    max(combined[1], current[1])
                ]
        
        result.append(combined)
        return result