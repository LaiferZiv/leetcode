class Solution:
    def climbStairs(self, n: int) -> int:
        sol,step1,step2 = 0,1,2
        if n <= 2:
            return 0 if n < 0 else n
        for _ in range(n-2):
            sol = step1 + step2
            step1 = step2
            step2 = sol
        return sol