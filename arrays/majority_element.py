# Majority Element


# Solution 1: Brute Force
# Double for loop to count the frequency of each element and check if it is a majority element.
# Time Complexity: O(n^2) | Space Complexity: O(1)
class Solution1:
    def majorityElement(self, nums):
        n = len(nums)
        for i in range(n):
            count = sum(1 for j in range(n) if nums[j] == nums[i])
            if count > n // 2:
                return nums[i]
        return -1  # No majority element found


# Solution 2: Hash Map
# Use a hash map to count the frequency of each element and check if it is a majority element.
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution2:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums) // 2:
                return num
        return -1  # No majority element found


# Solution 3: Sorting
# Sort the array and return the middle element.
# Time Complexity: O(n log n) | Space Complexity: O(1)
class Solution3:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


# Solution 4: Boyer-Moore Voting Algorithm
# Time Complexity: O(n) | Space Complexity: O(1)
# Intuition: If we pair different elements, they will cancel each other out. The majority element will be the one that remains at the end.
class Solution4:
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
