# Trapping Rain Water

class Solution:
    def trap(self, height):
        n = len(height)
        left = [0] * n
        right = [0] * n
        left[0] = height[0]
        right[n-1] = height[n-1]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - height[i]
        return water

    def trapOptimized(self, height):
        n = len(height)
        left = 0
        right = n - 1
        leftMax = 0
        rightMax = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right -= 1
        return water

if __name__ == '__main__':
    sol = Solution()

    # Test 1
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # Output: 6
    print(sol.trap(height))
    print(sol.trapOptimized(height))

    # Test 2
    height = [4,2,0,3,2,5]
    # Output: 9
    print(sol.trap(height))
    print(sol.trapOptimized(height))

    # Test 3
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # Output: 6
    print(sol.trap(height))
    print(sol.trapOptimized(height))
