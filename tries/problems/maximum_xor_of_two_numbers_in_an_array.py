# Maximum Xor with an element from an array



class TrieNode:
    def __init__(self):
        self.links = [None] * 2

    def containsKey(self, bit):
        return self.links[bit]

    def put(self, bit, node):
        self.links[bit] = node

    def get(self, bit):
        return self.links[bit]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.containsKey(bit):
                node.put(bit, TrieNode())
            node = node.get(bit)

    def findMaxXOR(self, num):
        node = self.root
        xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.containsKey(1 - bit):
                xor |= 1 << i
                node = node.get(1 - bit)
            else:
                node = node.get(bit)
        return xor

class Solution:
    # Time complexity: O(nlogn + qlogq + 32N + 32Q) -> O(nlogn + qlogq) | Space complexity: O(q)
    def maximizeXor(self, nums, queries):
        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        trie = Trie()
        res = [-1] * len(queries)
        j = 0
        for i, (x, m) in queries:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            res[i] = trie.findMaxXOR(x)
        return res


if __name__ == "__main__":
    sol = Solution()
    # Test 1
    nums = [4, 9, 2, 5, 0, 1]
    queries = [ [3, 0], [3, 10], [7, 5], [7,9] ]
    expectedOutput = [3, 10, 7, 14]
    output = sol.maximizeXor(nums, queries)
    print(f"Output: {output}, Expected: {expectedOutput}")

    # Test 2
    nums = [0, 1, 2, 3, 4]
    queries = [ [3, 1], [1, 3], [5, 6] ]
    expectedOutput = [3, 3, 7]
    output = sol.maximizeXor(nums, queries)
    print(f"Output: {output}, Expected: {expectedOutput}")
