# Insert Interval


# Time: O(nlogn) | Space: O(n))
class Solution:
    def insertNewInterval(self, intervals, new_interval):
        """
        Inserts a new interval into a list of sorted, non-overlapping intervals and merges them
        if necessary to maintain the non-overlapping property.

        Args:
        intervals (List[List[int]]): A list of non-overlapping intervals sorted by start time.
        new_interval (List[int]): A new interval to insert.

        Returns:
        List[List[int]]: A new list of non-overlapping intervals after merging.
        """
        # Copy the input list to avoid modifying it and append the new interval
        intervals = intervals[:]
        intervals.append(new_interval)

        # Sort intervals based on start times
        intervals.sort(key=lambda x: x[0])

        # Initialize variables
        n = len(intervals)
        merged_intervals = []  # To store the merged intervals
        i = 0  # Pointer to traverse the intervals

        # Iterate through all intervals
        while i < n:
            current_interval = intervals[i]  # The interval currently being processed
            start, end = current_interval[0], current_interval[1]  # Start and end of the current interval

            # Check for overlapping intervals
            j = i + 1
            while j < n:
                next_interval = intervals[j]  # The next interval to compare
                if end >= next_interval[0]:  # Overlap condition
                    # Merge intervals by extending the end time
                    end = max(end, next_interval[1])
                    i = j  # Move the pointer to the last merged interval
                    j += 1
                else:
                    break

            # Append the merged interval to the result
            merged_intervals.append([start, end])
            i += 1

        return merged_intervals
