"""─────────────────────────────
1. Overview of Merge Sort
─────────────────────────────
Merge Sort is a classic divide-and-conquer sorting algorithm. The key idea is to:
• Divide the unsorted list into two roughly equal halves.
• Recursively sort each half.
• Merge the two sorted halves into a single sorted list.

Because the merge operation is the heart of the algorithm, Merge Sort guarantees that the merging of two sorted lists is done efficiently. This approach consistently achieves a good performance regardless of the input ordering.

─────────────────────────────
2. How Merge Sort Works (Step-by-Step)
─────────────────────────────
a. Base Case:
   - If the list has one element or is empty, it is already sorted.
b. Divide:
   - Split the list into two halves.
c. Conquer:
   - Recursively apply Merge Sort to both halves.
d. Combine (Merge):
   - Merge the two sorted halves back together by comparing the elements one by one.

─────────────────────────────
3. Python Code Implementation
─────────────────────────────
Below is a simple and clear Python implementation of Merge Sort:

-----------------------------------------------------------"""
def merge_sort(arr):
    # Base case: if the list is of length 0 or 1, it is already sorted.
    if len(arr) <= 1:
        return arr

    # Divide: find the midpoint and split the list in half.
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer: merge the two sorted halves.
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    # Compare each element of the lists and merge them in sorted order.
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # If there are remaining elements in left or right, add them.
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Example usage:
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:  ", sorted_arr)
"""-----------------------------------------------------------

When you run the above code, it will print the original array and the sorted result.

─────────────────────────────
4. Time Complexity Analysis
─────────────────────────────
Merge Sort exhibits the following time complexities:
• Best-case: O(n log n)
• Average-case: O(n log n)
• Worst-case: O(n log n)

Explanation:
- Each level of recursion divides the list into halves (log n levels).
- At each level, the merging process takes O(n) time.
- Therefore, total work is roughly O(log n) * O(n) = O(n log n).

─────────────────────────────
5. Space Complexity Analysis
─────────────────────────────
Merge Sort is not an in-place sort (unless carefully implemented with linked structures) and typically requires additional space:
• Space Complexity: O(n)

Explanation:
- The extra space is used to hold copies of the arrays while merging.
- Recursive call stack space is O(log n), but since O(n) dominates, overall space complexity is O(n).

─────────────────────────────
6. Advantages of Merge Sort
─────────────────────────────
• Predictable performance with O(n log n) time in all cases.
• Stable sort: does not change the relative order of equal elements.
• Good for sorting linked lists because merging can be done without extra space for arrays.
• Suitable for external sorting (sorting data that does not fit into memory) due to sequential access patterns.

─────────────────────────────
7. Disadvantages of Merge Sort
─────────────────────────────
• Uses extra memory O(n) – not an in-place sorting algorithm.
• Can be relatively slower for small data sets due to the overhead of recursive calls and merging.
• The additional space overhead might be a constraint in memory-limited environments.

─────────────────────────────
8. Example Walkthrough
─────────────────────────────
Consider sorting the list [38, 27, 43, 3, 9, 82, 10]:

Step 1: Divide
   - Split into two halves: [38, 27, 43] and [3, 9, 82, 10]

Step 2: Recursively sort each half
   Sorting [38, 27, 43]:
     • Split into [38] and [27, 43]
     • [38] is already sorted.
     • Sorting [27, 43]:
         - Split into [27] and [43] (both sorted).
         - Merge to get [27, 43]
     • Merge [38] and [27, 43]:
         - Compare: 38 vs 27 → choose 27
         - Then compare 38 vs 43 → choose 38
         - Then append 43 → result: [27, 38, 43]

   Sorting [3, 9, 82, 10]:
     • Split into [3, 9] and [82, 10]
     • [3, 9] is sorted after merging [3] and [9].
     • Sorting [82, 10]:
         - Split into [82] and [10] (both sorted).
         - Merge: result becomes [10, 82]
     • Merge [3, 9] and [10, 82]:
         - Compare: 3 vs 10 → choose 3
         - Then 9 vs 10 → choose 9
         - Then append 10 and 82 → result: [3, 9, 10, 82]

Step 3: Final merge
   Merge [27, 38, 43] and [3, 9, 10, 82]:
     - Compare 27 vs 3 → choose 3
     - Compare 27 vs 9 → choose 9
     - Compare 27 vs 10 → choose 10
     - Compare 27 vs 82 → choose 27
     - Then 38, 43, and finally 82
   → Final Sorted List: [3, 9, 10, 27, 38, 43, 82]

─────────────────────────────
9. Additional Considerations
─────────────────────────────
• Variants:
  There are in-place variants of merge sort that reduce the auxiliary space requirement but are more complex to implement and may have a higher constant factor in time complexity.

• Applications:
  - Due to its stability and predictable O(n log n) behavior, Merge Sort is widely used in applications where deep recursion is not an issue and additional memory is available.
  - It is also useful in external sorting where data is stored on disk.

• Optimizations:
  - For smaller subarrays, switching to an algorithm like Insertion Sort may be advantageous to reduce overhead.
  - Tail recursion and iterative implementations can sometimes help optimize performance in certain environments.

─────────────────────────────
10. Conclusion
─────────────────────────────
Merge Sort is a robust sorting algorithm that guarantees O(n log n) performance and stability. Despite its extra space requirement, its predictable behavior and suitability for handling large datasets or external data make it a staple in the realm of sorting algorithms.

This concludes the deep dive into Merge Sort, covering everything from explanation and code to complexity analysis and practical examples."""
