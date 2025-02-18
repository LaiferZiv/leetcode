class Solution:
    def findMin(self, nums):
        left = mid = 0
        right = len(nums)-1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid
        return min(nums[left],nums[right])

