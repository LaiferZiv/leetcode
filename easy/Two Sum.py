class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            c = target-nums[i]
            if c in d:
                return [d[c],i]
            else:
                d[nums[i]] = i
