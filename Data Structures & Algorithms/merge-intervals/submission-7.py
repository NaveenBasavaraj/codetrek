class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for curr_start, curr_end in intervals:
            prev_end = res[-1][1]
            if prev_end >= curr_start:
                # overlap
                res[-1][1] = max(prev_end, curr_end)
            else:
                res.append([curr_start, curr_end])
            

        return res
        