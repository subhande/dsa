# Astroid Collision

"""
Explanation:

1. We iterate over each asteroid in the input list.
2. Within the loop, we check if there is a collision possibility (i.e. the current asteroid is negative while the last asteroid in the stack is positive).
3. If a collision occurs:
   - If the current asteroid (in absolute value) is larger, the asteroid at the top of the stack is removed. We continue checking with the new top of the stack.
   - If they are equal in absolute value, both explode (pop from stack and skip addition of the current asteroid).
   - If the current asteroid is smaller in absolute value, it explodes (we break out of the loop without adding it to the stack).
4. If no collision occurs (or after all collisions are resolved), we add the current asteroid to the stack.
5. Finally, the stack represents the state of asteroids after all collisions.

This implementation efficiently simulates the collision process with a time complexity of O(n) in the typical case.

"""

class Solution:
    def asteroidCollision(self, asteroids):
        # stack will hold the asteroids that haven't exploded yet
        stack = []
        for asteroid in asteroids:
            # check for potential collisions
            while stack and asteroid < 0 and stack[-1] > 0:
                # collision occurs: compare sizes (abs values)
                if abs(asteroid) > abs(stack[-1]):
                    # last asteroid in stack explodes, pop it and continue checking collision
                    stack.pop()
                    continue
                elif abs(asteroid) == abs(stack[-1]):
                    # both asteroids explode
                    stack.pop()
                # if abs(asteroid) is less than abs(stack[-1]), the incoming asteroid explodes
                break
            else:
                # no collision or collision was resolved without explosion of current asteroid
                stack.append(asteroid)
        return stack




if __name__ == '__main__':
    sol = Solution()

    # Test 1
    asteroids = [5, 10, -5]
    # Output: [5, 10]
    print(sol.asteroidCollision(asteroids))

    # Test 2
    asteroids = [8, -8]
    # Output: []
    print(sol.asteroidCollision(asteroids))

    # Test 3
    asteroids = [10, 2, -5]
    # Output: [10]
    print(sol.asteroidCollision(asteroids))

    # Test 4
    asteroids = [-2, -1, 1, 2]
    # Output: [-2, -1, 1, 2]
    print(sol.asteroidCollision(asteroids))
