# Majority Element


# Solution 1: Brute Force
# Double for loop to count the frequency of each element and check if it is a majority element.
# Time Complexity: O(n^2) | Space Complexity: O(1)

# Solution 2: Hash Map
# Use a hash map to count the frequency of each element and check if it is a majority element.
# Time Complexity: O(n) | Space Complexity: O(n)

# Solution 3: Sorting
# Sort the array and return the middle element.
# Time Complexity: O(n log n) | Space Complexity: O(1)

# Solution 4: Boyer-Moore Voting Algorithm
# Time Complexity: O(n) | Space Complexity: O(1)
# Intuition: If we pair different elements, they will cancel each other out. The majority element will be the one that remains at the end.
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

    def majorityElement2(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Check if the candidate is actually the majority element
        count = nums.count(candidate)
        if count <= len(nums) // 2:
            return -1  # No majority element found

        return candidate
