# Fruit Into Buskets
from typing import List
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = right = 0
        fruitBasket = defaultdict(int)
        n = len(fruits)
        maxFruits = 0
        while right < n:
            fruitBasket[fruits[right]] += 1

            if len(fruitBasket) > 2:
                fruitBasket[fruits[left]] -= 1
                if fruitBasket[fruits[left]] == 0:
                    fruitBasket.pop(fruits[left])
                left += 1

            maxFruits = max(maxFruits, right - left + 1)
            right += 1
        return maxFruits
