class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        mul = 1
        res = [1] * len(nums)
        for i in range(1,len(nums)):
            mul *= nums[i-1]
            res[i] *= mul
        mul = 1
        for i in range(len(nums)-2,-1,-1):
            mul *= nums[i+1]
            res[i] *= mul
        return res