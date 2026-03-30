# Dot Product of Two Sparse Vectors


from typing import List


# Approach 1: Non-Efficient Array Approach
# Time Complexity: O(n) | Space Complexity: O(n)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for ele1, ele2 in zip(self.vector, vec.vector):
            result += ele1 * ele2
        return result


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

# Approach 2: Hash Map Approach
# Time Complexity:
# - Initialization: O(n) | Space Complexity: O(L) where L is the number of non-zero elements in the vector
# - Dot Product: O(L) | Space Complexity: O(1)

class SparseVector2:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n

    def dotProduct(self, vec: 'SparseVector2') -> int:
        result = 0
        # iterate through each non-zero element in this sparse vector
        # update the dot product if the corresponding index has a non-zero value in the other vector
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]
        return result


# Approach 3:Index-Pair Approach
# Initialization: O(n) | Space Complexity: O(L+L2) where L and L2 are the number of non-zero elements in the two vectors
# Dot Product: O(L) | Space Complexity: O(1)

class SparseVector3:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for index, value in enumerate(nums):
            if value != 0:
                self.pairs.append([index, value])

    def dotProduct(self, vec: 'SparseVector3') -> int:
        result = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                result += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return result
