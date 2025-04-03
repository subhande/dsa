# N meeting in one room


class Solution:
    def maxMeetings(self, start, end):
        meetings = [(start[i], end[i]) for i in range(len(start))]
        meetings.sort(key=lambda x: x[1])
        validMeetings = []
        for meeting in meetings:
            if not validMeetings:
                validMeetings.append(meeting)
            else:
                lastMeeting = validMeetings[-1]
                if lastMeeting[-1] < meeting[0]:
                    validMeetings.append(meeting)
        return len(validMeetings)

class Solution2:
    # Function to find the maximum number of meetings that can be held
    def maxMeetings(self, start, end):
        n = len(start)
        # List to store meetings
        meetings = []

        # Fill the meetings list with start and end times
        for i in range(n):
            meetings.append((start[i], end[i]))

        # Sort the meetings based on end times in ascending order
        meetings.sort(key=lambda x: x[1])

        # The end time of last selected meeting
        limit = meetings[0][1]
        # Initialize count
        count = 1

        # Iterate through the meetings to select the maximum number of non-overlapping meetings
        for i in range(1, n):
            # If the current meeting starts after the last selected meeting ends
            if meetings[i][0] > limit:
                # Update the limit to the end time of the current meeting
                limit = meetings[i][1]
                # Increment count
                count += 1

        # Return count
        return count
