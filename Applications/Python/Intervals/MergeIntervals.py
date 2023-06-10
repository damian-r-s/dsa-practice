# 56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input

class Solution:
    def merger(self, first, second):
        return [
            min(first[0], second[0]),
            max(first[1], second[1])
        ]

    def overlap(self, first, second):
        if first[0] <= second[0] and second[0] <= first[1]:
            return True
        
        if second[0] <= first[0] and first[0] <= second[1]:
            return True

        return False

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =  lambda row: row[0])

        result = []
        combined = intervals[0]

        for i in range(1, len(intervals)):            
            current = intervals[i]

            if self.overlap(current, combined):
                combined = self.merger(current, combined)
            else:
                result.append(combined)
                combined = current

        result.append(combined)

        return result

