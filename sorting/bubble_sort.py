"""Bubble sort is one of the simplest sorting algorithms. It works by repeatedly stepping through the list, comparing adjacent items, and swapping them if they are in the wrong order. The process is repeated until no swaps are needed, which means the list is sorted.

--------------------------------"""

"""
Compare with Next Element and Swap if Necessary
Initial: [5, 1, 4, 2, 8]

Pass 1:
 compare 5 & 1 -> swap -> [1, 5, 4, 2, 8]
 compare 5 & 4 -> swap -> [1, 4, 5, 2, 8]
 compare 5 & 2 -> swap -> [1, 4, 2, 5, 8]
 compare 5 & 8 -> no swap -> [1, 4, 2, 5, 8]
 After pass 1, 8 is in correct final position.

Pass 2:
 compare 1 & 4 -> no swap -> [1, 4, 2, 5, 8]
 compare 4 & 2 -> swap -> [1, 2, 4, 5, 8]
 compare 4 & 5 -> no swap -> [1, 2, 4, 5, 8]
 After pass 2, 5 is in correct place.

Pass 3:
 compare 1 & 2 -> no swap
 compare 2 & 4 -> no swap
 No swaps this pass -> array is sorted: [1, 2, 4, 5, 8]

"""

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Track whether any swap took place in this iteration
        swapped = False
        # Last i elements are already sorted so we ignore them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then the list is sorted
        if not swapped:
            break
    return arr

# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Sorted list:", sorted_list)

"""--------------------------------
Time Complexity:

1. Worst Case:
   - Occurs when the array is sorted in reverse order.
   - For every element, the inner loop compares and swaps nearly every other element.
   - The complexity is O(n²).

2. Average Case:
   - In an average scenario, the number of comparisons and swaps is still proportional to the square of the number of elements.
   - Hence, the time complexity remains O(n²).

3. Best Case:
   - Occurs when the array is already sorted.
   - With a modified version that includes a swapped flag (as shown above), the algorithm can detect no swaps in the first pass and terminate early.
   - This leads to a best-case time complexity of O(n) because the algorithm only needs one pass through the array.

--------------------------------
Space Complexity:

- Bubble sort operates by modifying the list in place.
- Only a few extra variables (like the swapped flag) are used, regardless of the input size.
- Therefore, the space complexity is O(1), meaning it requires constant extra space.

--------------------------------
Summary:

- Time Complexity:
  - Worst-case: O(n²)
  - Average-case: O(n²)
  - Best-case (optimized): O(n)
- Space Complexity: O(1)

Bubble sort is simple to understand and implement, but its quadratic time complexity makes it inefficient for large datasets compared to more advanced sorting algorithms like merge sort, quicksort, or heapsort."""
