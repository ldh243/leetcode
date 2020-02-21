class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        F = [9999999] * len(cost)
        for i, val in enumerate(cost):
            if i == 0 or i == 1:
                F[i] = cost[i]
            else:
                F[i] = min(F[i-2], F[i-1]) + val
        return F[len(cost)-1]