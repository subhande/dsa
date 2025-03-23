# Frog Jump (Jump Game Variation)
# https://takeuforward.org/plus/dsa/dynamic-programming/1d-dp/frog-jump

class Solution:
    def frogJump(self, heights):
        total_steps = len(heights)
        if total_steps == 0 or total_steps == 1:
            return 0
        if total_steps == 2:
            return abs(heights[0]-heights[1])
        one_step_back = abs(heights[0]-heights[1])
        two_step_back = 0

        for i in range(2, total_steps):
            current_energy = min(
                one_step_back + abs(heights[i]-heights[i-1]),
                two_step_back + abs(heights[i]-heights[i-2])
            )
            two_step_back = one_step_back
            one_step_back = current_energy
        return one_step_back
