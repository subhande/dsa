"""Quick Sort is a highly efficient, comparison-based, divide-and-conquer sorting algorithm. Here’s an in-depth explanation along with Python code, complexity analysis, advantages and disadvantages, examples, and more details.

Pick a pivot, put smaller elements left and larger right, then repeat recursively.

──────────────────────────────
1. Explanation

• The algorithm works by selecting a “pivot” element from the array.
• The array is then partitioned into two sub-arrays:
  – Elements less than the pivot
  – Elements greater than the pivot
• The pivot is now in its correct sorted position.
• The algorithm recursively applies the same logic to the sub-arrays until the entire array is sorted.

The choice of the pivot can vary (first element, last element, random element, or median-of-three). A good pivot choice generally leads to better performance.

──────────────────────────────
2. Python Code

Below are two common implementations:

A. Recursive Quick Sort Using Extra Space
(This version uses list comprehensions and is very concise, though it is not in-place.)

------------------------------------------------
def quick_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Choose the pivot (here, we pick the middle element)
        pivot = arr[len(arr) // 2]
        # Partition the array into three parts
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Recursively sort and combine the results
        return quick_sort(left) + middle + quick_sort(right)

# Example:
lst = [33, 10, 59, 25, 72, 18, 10]
sorted_lst = quick_sort(lst)
print("Sorted array:", sorted_lst)
------------------------------------------------

B. In-Place Quick Sort
(This version modifies the array without using extra lists; it is more space-efficient.)

------------------------------------------------"""
def partition(arr, low, high):
    # Use the last element as pivot
    pivot = arr[high]
    i = low - 1  # pointer for greater element
    for j in range(low, high):
        # If current element is <= pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_helper(arr, low, high):
    if low < high:
        # Partition the array and get pivot index
        pi = partition(arr, low, high)
        # Recursively apply to sub-arrays
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)

def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)

# Example:
lst = [33, 10, 59, 25, 72, 18, 10]
quick_sort(lst)
print("Sorted array:", lst)
"""------------------------------------------------

──────────────────────────────
3. Time Complexity Analysis

• Best Case: O(n log n)
  – Occurs when the pivot always splits the array into two nearly equal halves.

• Average Case: O(n log n)
  – Many pivot choices tend to lead to balanced partitions over many runs.

• Worst Case: O(n²)
  – Occurs when the pivot is the smallest or largest element (e.g., already sorted array with a poor pivot selection).

──────────────────────────────
4. Space Complexity Analysis

• Recursive (concise) Version:
  – Uses extra space for the sub-arrays; space complexity can be O(n) in the worst case.

• In-Place Version:
  – Only uses O(log n) space on average due to recursion stack; worst-case recursion depth is O(n) (which can be mitigated with techniques like tail recursion optimization or randomized pivot selection).

──────────────────────────────
5. Advantages

• Average-case performance is excellent at O(n log n).
• In-place version requires little additional memory.
• Quick sort typically has a smaller constant factor than other sorting algorithms (e.g., Merge Sort).
• It is a well-known and widely-used algorithm in practice.

──────────────────────────────
6. Disadvantages

• Worst-case performance is O(n²) if the pivot selection is poor (e.g., sorted input with naive pivot selection).
• It is not a stable sort by default; equal elements’ relative order may not be preserved (stability can be maintained with extra techniques, though at a cost).
• Recursive algorithm might lead to stack overflow on very large arrays if not implemented carefully (e.g., by using iterative approaches or tail call optimization).

──────────────────────────────
7. Example Walkthrough

Consider the array: [33, 10, 59, 25, 72, 18, 10]

Using the recursive version with the middle element as pivot:
• First call:
  – Pivot: 25
  – Partitioning gives:
    Left: [10, 18, 10]
    Middle: [25]
    Right: [33, 59, 72]
• Recursively sort both left and right:
  – For left [10, 18, 10]:
    Pivot might be 18 → after partitioning: [10, 10] and [18]
  – For right [33, 59, 72]:
    Pivot might be 59 → after partitioning: [33] and [72]
• Combining these, the fully sorted array becomes: [10, 10, 18, 25, 33, 59, 72]

──────────────────────────────
8. More Details / Variations

• Pivot Selection:
  – Randomized Quick Sort: Randomly select a pivot to help avoid the worst-case scenario.
  – Median-of-three: Choose the median of the first, middle, and last elements.

• Hybrid Algorithms:
  – Some sorting libraries switch to insertion sort for small sub-arrays since insertion sort can be faster for small datasets.

• Tail Recursion:
  – Optimizing the recursion call can reduce the stack depth. In some languages, tail-recursive optimizations can be beneficial.

• Applications:
  – Quick Sort is used in many standard libraries (with modifications to account for worst-case scenarios) due to its efficiency in practical applications.

──────────────────────────────
Conclusion

Quick sort is an excellent general-purpose sorting algorithm, particularly known for its average-case efficiency and in-place sorting capability. While it has potential pitfalls in terms of worst-case performance, careful implementation (e.g., randomized pivot selection) usually results in an algorithm that is both fast and efficient for large datasets.

This concludes the brief explanation, Python code examples, time and space complexity analysis, as well as the advantages and disadvantages of Quick sort."""


"""
Array: [33, 10, 59, 25, 72, 18, 10]

Pass 1:
- Choose pivot(last element): 10
- Partitioning:
- Compare 33 with 10 -> 33 > 10, no swap
- Compare 10 with 10 -> 10 <= 10, swap with itself (i = 0)
- Compare 59 with 10 -> 59 > 10, no swap
- Compare 25 with 10 -> 25 > 10, no swap
- Compare 72 with 10 -> 72 > 10, no swap
- Compare 18 with 10 -> 18 > 10, no swap
- Swap pivot with element at i+1 (10 with 10)
Array after Pass 1: [10, 10, 59, 25, 72, 18, 33]
Partition index: 1
Left sub-array: [10]
Right sub-array: [59, 25, 72, 18, 33]

Pass 2 (Right sub-array):
- Choose pivot(last element): 33
- i = 1 (starting index of right sub-array)
- Partitioning:
- Compare 59 with 33 -> 59 > 33, no swap
- Compare 25 with 33 -> 25 <= 33, swap with itself (i = 2) -> [10, 10, 25, 59, 72, 18, 33]
- Compare 72 with 33 -> 72 > 33, no swap
- Compare 18 with 33 -> 18 <= 33, swap with itself (i = 3) -> [10, 10, 25, 18, 72, 59, 33]
- Swap pivot with element at i+1 (33 with 59)
Array after Pass 2: [10, 10, 25, 18, 33, 72, 59]
Partition index: 4
Left sub-array: [25, 18]
Right sub-array: [72, 59]

"""
