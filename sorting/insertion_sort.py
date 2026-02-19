# Insertion Sort
#
#
#
def insertion_sort(arr):
    """
    Sorts the list 'arr' in ascending order using the insertion sort algorithm.

    Parameters:
      arr (list): The list of elements to be sorted.

    Returns:
      list: The sorted list.
    """
    # Traverse from index 1 to the end of the list
    for i in range(1, len(arr)):
        key = arr[i]  # The element we want to insert into the sorted (left) part of the array
        j = i - 1

        # Move elements of arr[0 ... i-1] that are greater than key to one position ahead
        # of their current position.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct location
        arr[j + 1] = key

    return arr

# Example usage:
if __name__ == "__main__":
    sample_list = [12, 11, 13, 5, 6]
    sorted_list = insertion_sort(sample_list)
    print("Sorted List:", sorted_list)

"""------------------------------------------------------------
Time Complexity:

1. Worst-case:
   • The worst-case occurs when the array is sorted in reverse order.
   • For each element, you compare it with all previously sorted elements.
   • Time complexity: O(n^2)

2. Best-case:
   • The best-case occurs when the array is already sorted.
   • In this case, the inner loop only makes one comparison per element.
   • Time complexity: O(n)

3. Average-case:
   • On average, the time complexity is also O(n^2) since half of the elements may need to be shifted.

------------------------------------------------------------
Space Complexity:

• Insertion sort is an in-place sorting algorithm.
• It requires only a constant amount of additional memory aside from the input array.
• Space complexity: O(1)

------------------------------------------------------------
Explanation:

- The algorithm starts at the second element (index 1) and treats the subarray before it as sorted.
- For each element, it finds the correct position in the sorted portion by comparing and shifting elements.
- After finding the correct position, it inserts the element.
- The process is repeated for all elements until the entire array is sorted.

This makes insertion sort simple and efficient for small or nearly-sorted datasets, even though it performs poorly on large and/or randomly ordered arrays due to its quadratic time complexity in the average and worst cases."""


"""
Arr: 5 2 4 6 1 3
Pass 1:
  key = 2, j = 0
  compare 2 & 5 -> shift 5 to the right -> [5, 5, 4, 6, 1, 3]
  insert 2 at position j+1 -> [2, 5, 4, 6, 1, 3]
Pass 2:
  key = 4, j = 1
  compare 4 & 5 -> shift 5 to the right -> [2, 5, 5, 6, 1, 3]
  insert 4 at position j+1 -> [2, 4, 5, 6, 1, 3]
Pass 3:
  key = 6, j = 2
  compare 6 & 5 -> no shift -> [2, 4, 5, 6, 1, 3]
Pass 4:
  key = 1, j = 3
  compare 1 & 6 -> shift 6 to the right -> [2, 4, 5, 6, 6, 3]
  compare 1 & 5 -> shift 5 to the right -> [2, 4, 5, 5, 6, 3]
  compare 1 & 4 -> shift 4 to the right -> [2, 4, 4, 5, 6, 3]
  compare 1 & 2 -> shift 2 to the right -> [2, 2, 4, 5, 6, 3]
  insert 1 at position j+1 -> [1, 2, 4, 5, 6, 3]
Pass 5:
  key = 3, j = 4
  compare 3 & 6 -> shift 6 to the right -> [1, 2, 4, 5, 6, 6]
  compare 3 & 5 -> shift 5 to the right -> [1, 2, 4, 5, 5, 6]
  compare 3 & 4 -> shift 4 to the right -> [1, 2, 4, 4, 5, 6]
  compare 3 & 2 -> no shift -> [1, 2, 4, 4, 5, 6]
  insert 3 at position j+1 -> [1, 2, 3, 4, 5, 6]
"""
