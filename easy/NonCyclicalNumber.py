class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            if n == 1:
                return True
            n = self.next_n(n)
        return False
    def next_n(self,n):
        sol = 0
        while n != 0:
            sol += (n%10)**2
            n //= 10
        return sol
