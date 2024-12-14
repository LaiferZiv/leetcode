class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if not cost:
            return 0
        elif len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost[0],cost[1])
        for i in range(2,len(cost)):
            cost[i] += min(cost[i-2], cost[i-1])
        return min(cost[-1],cost[-2])
