
# Minimum number of platforms required for a railway



class Solution:
    def findPlatform(self, Arrival, Departure):

        trains = [(int(Arrival[i]), int(Departure[i])) for i in range(len(Arrival))]
        trains.sort(key=lambda x: x[0])
        n = len(trains)
        platforms = [-1] * n
        # platforms[0] = trains[0][1]

        for idx in range(n):

            train_arr_time, train_dep_time =  trains[idx]

            for platform_idx in range(len(platforms)):

                last_train_dep_time = platforms[platform_idx]
                if train_arr_time > last_train_dep_time:

                    platforms[platform_idx] = train_dep_time

                    break

        return len([platform for platform in platforms if platform != -1])


# Time: O(nlogn) + O(nm) => O(n^2) | Spcae: O(n)
class Solution2:
    def findPlatform(self, arrival, departure):
        """
        Determines the minimum number of platforms required at a railway station so that
        no train is kept waiting.

        Args:
        arrival (List[int]): List of arrival times of trains (24-hour format).
        departure (List[int]): List of departure times of trains (24-hour format).

        Returns:
        int: Minimum number of platforms required.
        """

        # Number of trains
        num_trains = len(arrival)

        # List to hold train schedules as (arrival, departure) tuples
        train_schedules = []

        # Create a combined list of arrival and departure times
        for i in range(num_trains):
            train_schedules.append((arrival[i], departure[i]))

        # Sort trains by their arrival times
        train_schedules.sort(key=lambda schedule: schedule[0])

        # List to track the departure time of trains using each platform
        platform_departure_times = []

        # Iterate through all the trains
        for i in range(num_trains):
            train_arrival = train_schedules[i][0]
            train_departure = train_schedules[i][1]
            platform_found = False

            # Check if any platform is free for this train
            for j in range(len(platform_departure_times)):
                if platform_departure_times[j] < train_arrival:
                    # Update the departure time of this platform
                    platform_departure_times[j] = train_departure
                    platform_found = True
                    break

            # If no platform was found, allocate a new platform
            if not platform_found:
                platform_departure_times.append(train_departure)

        # The number of platforms in use is the answer
        return len(platform_departure_times)
