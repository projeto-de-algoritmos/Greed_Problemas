class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removal_count = 0
        sorted_intervals = sorted(intervals, key=lambda x: x[0], reverse=True)
        result = [sorted_intervals[0]]
        for start, end in sorted_intervals[1:]:
            if result[-1][0] >= end: 
                result.append([start, end])
            else: 
                removal_count += 1
        return removal_count