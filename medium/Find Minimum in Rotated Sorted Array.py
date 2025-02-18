class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left,right = 0,len(nums)-1
        while right-left > 1:
            mid = (left+right)//2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] < nums[left]:
                left = mid
        return min(nums[left],nums[right])