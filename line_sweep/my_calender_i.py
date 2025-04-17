# My Calender I

class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            self.events.append((startTime, endTime))
            return True

        for event in self.events:
            existingEventStartTime, existingEventEndTime = event

            low = max(existingEventStartTime, startTime)
            high = min(existingEventEndTime, endTime)

            if low < high:
                return False
        self.events.append((startTime, endTime))

        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)


from sortedcontainers import SortedList

class MyCalendar2:
    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.calendar.bisect_right((start, end))
        if (idx > 0 and self.calendar[idx-1][1] > start) or (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
        self.calendar.add((start, end))
        return True
