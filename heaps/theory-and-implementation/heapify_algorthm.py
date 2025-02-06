"""
# Heapify Algorithm

Given an array arr representing a min-heap and two integers ind and val, set the value at index ind (0-based) to val and perform the heapify algorithm such that the resulting array follows the min-heap property.

Modify the original array in-place, no need to return anything.


Examples:
---------------------------------------
Input: arr = [1, 4, 5, 5, 7, 6], ind = 5, val = 2
Output: [1, 4, 2, 5, 7, 5]

Explanation: After setting index 5 to 2, the resulting heap in array form = [1, 4, 5, 5, 7, 2]
Parent of arr[5] = arr[2] = 5 > arr[5] = 2, so they are swapped.
Final array = [1, 4, 2, 5, 7, 5]
---------------------------------------
Input: arr = [2, 4, 3, 6, 5, 7, 8, 7], ind = 0, val = 7
Output: [3, 4, 7, 6, 5, 7, 8, 7]

Explanation: After setting index 0 to 7, the resulting heap in array form =[7, 4, 3, 6, 5, 7, 8, 7]
The parent of arr[2] = arr[0] = 7 > arr[2] = 3, so they are swapped. No further swaps are needed.
Final array = [3, 4, 7, 6, 5, 7, 8, 7]
---------------------------------------

Constraints:
-> 1 <= arr.length <= 105
-> -104 <= arr[i] <= 104
-> 0 <= ind < arr.length
-> -104 <= val <= 104
-> arr represents a min-heap
"""


class Solution:
    # Define the heapify-up function (used when a value is decreased)
    def heapify_up(self, arr, i):
        """Moves the node at index i up if it violates the min-heap property."""
        parent = (i - 1) // 2  # Calculate the parent index
        if i > 0 and arr[parent] > arr[i]:
            # Swap if parent is greater than the current node
            arr[parent], arr[i] = arr[i], arr[parent]
            # Move upwards
            i = parent
            parent = (i - 1) // 2  # Recalculate the new parent index
            self.heapify_up(arr, i)

    # Define the heapify-down function (used when a value is increased)
    def heapify_down(self, arr, i):
        """Moves the node at index i down if it violates the min-heap property."""
        n = len(arr)  # Length of the heap
        smallest = i  # Assume the current node is the smallest
        left = 2 * i + 1  # Left child index
        right = 2 * i + 2  # Right child index

        # Check if left child is smaller than the current node
        if left < n and arr[left] < arr[smallest]:
            smallest = left
        # Check if right child is smaller than the smallest found so far
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        # If the current node is already the smallest, stop heapifying
        if smallest == i:
            return

        # Swap the current node with the smallest child and continue down
        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest  # Move to the next node to continue heapifying
        self.heapify_down(arr, i)

    def heapify(self, arr, ind, val):
        """
        Modifies the value at index `ind` to `val` and ensures the min-heap property is maintained.
        """
        # Update the value at index ind
        arr[ind] = val

        # Determine whether to heapify-up or heapify-down
        parent = (ind - 1) // 2  # Calculate the parent index
        if ind > 0 and arr[parent] > arr[ind]:
            # If the updated value is smaller than its parent, bubble up
            self.heapify_up(arr, ind)
        else:
            # If the updated value is larger than a child, bubble down
            self.heapify_down(arr, ind)


# Driver code
if __name__ == "__main__":
    arr = [1, 4, 5, 5, 7, 6]
    ind, val = 5, 2

    # Input array
    print("Input array:", arr)

    # Creating an object of the Solution class
    sol = Solution()

    # Function call to heapify the array
    sol.heapify(arr, ind, val)

    # Output array
    print("Modified array after heapifying:", arr)
