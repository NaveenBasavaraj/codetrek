class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]

        for curr_start, curr_end in intervals[1:]:
            if curr_start >= prev_end:
                prev_end = curr_end
            else:
                res += 1
                prev_end = min(curr_end, prev_end)
        return res