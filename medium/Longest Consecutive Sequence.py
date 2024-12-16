class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            lenth = 1
            while num+lenth in s:
                lenth += 1
            longest = max(lenth,longest)
        return longest