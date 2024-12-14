class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        sol = 0
        for num in nums:
            sol ^= num
        return sol