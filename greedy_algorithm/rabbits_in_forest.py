# Rabbits in the Forest
# https://leetcode.com/problems/rabbits-in-forest/

from collections import defaultdict  # to count how many times each answer appears
import math                          # for the ceiling function
from typing import List              # for type hints

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        Compute the minimum number of rabbits in the forest given
        each rabbit's answer about how many others share its color.
        """

        # Build a frequency map: answer -> number of rabbits giving that answer
        frequency_map = defaultdict(int)
        for answer in answers:
            frequency_map[answer] += 1

        total_rabbits = 0  # accumulator for the final count

        # For each distinct reported answer and its frequency:
        for answer, frequency in frequency_map.items():
            # If a rabbit says 'answer', then there are (answer + 1) rabbits
            # of that color in one complete group
            group_size = answer + 1

            # Determine how many such groups are needed to cover all rabbits
            num_groups = math.ceil(frequency / group_size)

            # Add the rabbits from these groups to the total
            total_rabbits += num_groups * group_size

        return total_rabbits