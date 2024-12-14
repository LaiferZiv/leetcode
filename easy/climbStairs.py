class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(history,num):
            if num < 0:
                return 0
            if num <= 2:
                history[num] = num
                return history[num]
            if history[num] != 0:
                return history[num]
            history[num] = dfs(history,num-1) + dfs(history,num-2)
            return history[num]
        history = [0] * (n+1)
        return dfs(history,n)