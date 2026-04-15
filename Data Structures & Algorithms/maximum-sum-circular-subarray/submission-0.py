class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        global_max = nums[0]
        global_min = nums[0]
        curr_max, curr_min = 0, 0
        total = 0

        for num in nums:
            curr_max = max(curr_max+num, num)
            curr_min = min(curr_min+num, num)
            total += num
            global_max = max(global_max, curr_max)
            global_min = min(global_min, curr_min)
        
        if global_max > 0:
            return max(global_max, total-global_min)
        else:
            return global_max