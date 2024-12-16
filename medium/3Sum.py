class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i,num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            left,right = i+1,len(nums)-1
            while left < right:
                val = num + nums[right] + nums[left]
                if val < 0:
                    left += 1
                elif val > 0:
                    right -= 1
                else:
                    res.append([num,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return res