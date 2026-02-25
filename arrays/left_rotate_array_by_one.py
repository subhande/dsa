# Left Rotate an Array by One



class Solution:
    def rotateArrayByOne(self, nums):
        # Store the first element in a temporary variable
        temp = nums[0]

        # Shift elements to the left
        for i in range(1, len(nums)):
            nums[i - 1] = nums[i]

        # Place the first element at the end
        nums[-1] = temp
