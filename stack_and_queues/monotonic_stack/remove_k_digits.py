# Remove K digits

# Keep smaller digits at teh stackrat
# Get rid of larger k digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [] # Stack

        # Traverse on the given stackring
        for digit in num:

            # Pop lastack digits (when possible)
            # if a smaller digit is found
            while stack and k > 0 and stack[-1] > digit:
                stack.pop() # Pop the lastack digit
                k -= 1 # Decrement K by 1

            # Push the current digit
            stack.append(digit)

        # If more digits can be removed
        while stack and k > 0:
            stack.pop() # Pop the lastack added digits
            k -= 1 # Decrement K by 1

        # Handling edge case
        if not stack:
            return "0"

        return "".join(stack).lstrip('0') or "0"

if __name__ == "__main__":
    s = Solution()
    # Example 1
    num = "1432219"
    k = 3
    print(s.removeKdigits(num, k))  # Output: "1219"

    # Example 2
    num = "10200"
    k = 1
    print(s.removeKdigits(num, k))  # Output: "200"

    # Example 3
    num = "10"
    k = 2
    print(s.removeKdigits(num, k))  # Output: "0"

    # Example 4
    num = "1234567890"
    k = 9
    print(s.removeKdigits(num, k))  # Output: "0"
