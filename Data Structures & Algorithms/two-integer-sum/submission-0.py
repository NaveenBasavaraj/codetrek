class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i, v in enumerate(nums):
            k = target - v
            if k in seen:
                return [seen[k], i]
            else:
                seen[v] = i
