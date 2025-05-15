# Corporate Flight Bookings
from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * (n+1)

        for booking in bookings:
            first, last, seats = booking
            print([booking], flights)
            flights[first] += seats

            if last+1 < n:
                flights[last+1] -= seats

        for i in range(1, n+1):
            flights[i] += flights[i-1]

        return flights[1:]


class Solution2:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * n

        for booking in bookings:
            first, last, seats = booking

            flights[first-1] += seats

            if last < n:
                flights[last] -= seats

        for i in range(1, n):
            flights[i] += flights[i-1]

        return flights
