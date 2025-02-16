"""Selection sort is a simple comparison‐based sorting algorithm. Its idea is to divide the list into two parts—a sorted section at the beginning and an unsorted section at the end. Initially, the sorted section is empty, and the entire list is unsorted. The algorithm repeatedly selects the smallest (or largest, depending on sorting order) element from the unsorted section and swaps it with the leftmost element of the unsorted section, thus growing the sorted section by one element.

Here’s how the algorithm works step by step:

1. Start with the first element (index 0) as the beginning of the unsorted array.
2. Find the smallest element in the unsorted part of the array.
3. Swap the smallest element with the element at the beginning of the unsorted section.
4. Move the boundary between the sorted and unsorted sections one element to the right.
5. Repeat the process until the whole array is sorted.

For example, consider sorting the array [29, 10, 14, 37, 13]:

• First Pass:
  - The unsorted section is [29, 10, 14, 37, 13].
  - The smallest element is 10.
  - Swap 10 with the first element (29), resulting in [10, 29, 14, 37, 13].

• Second Pass:
  - The unsorted section is now [29, 14, 37, 13] (starting at index 1).
  - The smallest element in this section is 13.
  - Swap 13 with 29, resulting in [10, 13, 14, 37, 29].

• Third Pass:
  - The unsorted section is [14, 37, 29] (starting at index 2).
  - The smallest element here is 14, which is already in the correct position.
  - No swap is needed (or you could swap it with itself).

• Fourth Pass:
  - The unsorted section is [37, 29] (starting at index 3).
  - The smallest element is 29.
  - Swap 29 with 37, resulting in [10, 13, 14, 29, 37].

Once all passes are complete, the array is fully sorted.

The basic pseudocode for selection sort is:

   for i = 0 to n - 2:
       minIndex = i
       for j = i + 1 to n - 1:
           if array[j] < array[minIndex]:
               minIndex = j
       if minIndex != i:            // Optional check to avoid unnecessary swaps
           swap array[i] and array[minIndex]

Time Complexity:
• Worst-case: O(n²)
• Best-case: O(n²)
• Average-case: O(n²)

Space Complexity: O(1) (selection sort is an in-place sorting algorithm)

Stability: The traditional selection sort is not stable. (Stability in sorting means that equal elements retain their relative order after sorting.)

Below is an example of selection sort implemented in Python:

-------------------------------------------------"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the element at i is the minimum.
        min_index = i
        # Find the minimum element in the rest of the array.
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first unsorted element.
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage:
arr = [29, 10, 14, 37, 13]
sorted_arr = selection_sort(arr)
print(sorted_arr)  # Output: [10, 13, 14, 29, 37]
"""-------------------------------------------------

Selection sort is best suited for small datasets or when memory write operations are costly, as it makes at most O(n) swaps. However, for larger datasets, more efficient algorithms like quicksort, mergesort, or heapsort are generally preferred."""
