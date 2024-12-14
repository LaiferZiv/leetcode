class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        bits_amount = 32
        for i in range(bits_amount):
            if (n >> i) & 1 == 1:
                ans += 1
        return ans
