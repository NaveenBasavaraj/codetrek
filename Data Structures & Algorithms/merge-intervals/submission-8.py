class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            last_intervals_end = res[-1][1]

            if last_intervals_end >= curr_start:
                # overlap
                res[-1][1] = max(curr_end, last_intervals_end)
            else:
                res.append([curr_start, curr_end])
        return res