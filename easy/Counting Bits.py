class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        power2 = 1
        for i in range(1,n+1):
            if power2 * 2 == i:
                power2 *= 2
            ans[i] = 1 + ans[i-power2]
        return ans