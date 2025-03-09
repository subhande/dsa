# Metting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/description/?envType=problem-list-v2&envId=prefix-sum

from typing import List

# Time complexity: O(n^2) | Space complexity: O(n)
class Solution1:
    def checkOverlapping(self, meeting_1: List[int], meeting_2: List[int]) -> bool:
        return False if meeting_2[0] >= meeting_1[1] else True

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        rooms = []
        for interval in intervals:
            if not rooms:
                rooms.append([interval])
            else:
                available = False
                for room in rooms:
                    if self.checkOverlapping(room[-1], interval) is False:
                        available = True
                        room[0] = interval
                        break

                if available is False:
                    rooms.append([interval])
        return len(rooms)


from heapq import heappush, heappop
from typing import List

class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort the intervals by their start times.
        intervals.sort(key=lambda x: x[0])

        # Initialize a min-heap.
        heap = []

        # Add the end time of the first meeting.
        heappush(heap, intervals[0][1])

        # Process the remaining meetings.
        for interval in intervals[1:]:
            # If the room with the earliest end time is free, reuse it.
            if interval[0] >= heap[0]:
                heappop(heap)
            # Allocate the room (either a new one or the reused one) by pushing the new end time.
            heappush(heap, interval[1])

        # The heap size is the number of rooms required.
        return len(heap)
