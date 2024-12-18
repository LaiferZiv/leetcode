class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(opens,close,tmp):
            if opens < 0 or close < 0 or opens > close:
                return
            if opens == 0 and close == 0:
                res.append(tmp)
                return
            dfs(opens-1,close,tmp + '(')
            dfs(opens, close-1, tmp + ')')
        res = []
        dfs(n,n,"")
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))
