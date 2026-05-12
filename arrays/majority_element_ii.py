from collections import defaultdict
from typing import List


# Approach 1: Hash Map
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution1:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        threshold = int(len(nums) / 3)
        result = set()
        for num in nums:
            freq[num] += 1
            if freq[num] > threshold:
                result.add(num)
        return list(result)


# Approach 2: Sorting
# Time Complexity: O(n log n) | Space Complexity: O(1)
class Solution2:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = int(len(nums) / 3)
        result = []
        nums.sort()
        currentElement = nums[0]
        currentElementCount = 1
        for idx in range(1, len(nums)):
            if currentElement != nums[idx]:
                if currentElementCount > threshold:
                    result.append(currentElement)
                currentElement = nums[idx]
                currentElementCount = 1
            else:
                currentElementCount += 1

        if currentElementCount > threshold:
            result.append(currentElement)

        return result


# Approach 3: Boyer-Moore Voting Algorithm
# Time Complexity: O(n) | Space Complexity: O(1)
class Solution3:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Step 1: Find potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidates
        result = []
        for candidate in [candidate1, candidate2]:
            if nums.count(candidate) > len(nums) // 3:
                result.append(candidate)

        return result
