class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits)-1
        digits[i] += 1
        while digits[i] == 10:
            digits[i] = 0
            if i != 0 :
                digits[i-1] += 1
            else:
                return [1] + digits
            i -= 1
        return digits



