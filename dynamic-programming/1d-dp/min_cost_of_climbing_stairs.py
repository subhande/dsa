# Min Cost Of Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_steps = len(cost)
        if total_steps <= 1:
            return 0

        cost_two_steps_back = 0  # Cost to reach two steps before
        cost_one_step_back = 0   # Cost to reach one step before

        for current_step in range(2, total_steps + 1):
            cost_to_current_step = min(
                cost_one_step_back + cost[current_step - 1],
                cost_two_steps_back + cost[current_step - 2]
            )
            cost_two_steps_back = cost_one_step_back
            cost_one_step_back = cost_to_current_step

        return cost_one_step_back
"""
--------------------------------------------------

• total_steps clearly represents the total number of steps.
• cost_two_steps_back and cost_one_step_back indicate the minimum cost to reach the two steps before and one step before the current step respectively.
• cost_to_current_step represents the computed minimum cost to reach the current step using the given recurrence relation.
"""
