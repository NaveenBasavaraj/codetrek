class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        res = [intervals[0]]

        for interval in intervals:
            curr_start = interval[0]
            curr_end = interval[1]

            prev_end = res[-1][1]

            if prev_end >= curr_start:
                res[-1][1] = max(prev_end, curr_end)
            else:
                res.append([curr_start, curr_end])
        return res