class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        if not numbers:
            return [-1,-1]
        left, right = 0, len(numbers) - 1
        while left < right:
            val = numbers[left] + numbers[right]
            if val == target:
                return [left,right]
            elif val < target:
                left += 1
            else:
                right -= 1
        return [-1,-1]