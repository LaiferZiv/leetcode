import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        if not piles:
            return 0
        top = k = max(piles)
        bottom = math.ceil(float(sum(piles))/h)
        while bottom <= top:
            k = (bottom+top)//2
            h_tmp = h
            for val in piles:
                h_tmp -= math.ceil(float(val)/k)
            if h_tmp >= 0:
                top = k-1
            else:
                bottom = k+1
        return k