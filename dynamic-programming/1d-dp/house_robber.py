# House robber
# https://takeuforward.org/plus/dsa/dynamic-programming/1d-dp/house-robber


class Solution:
    def houseRobber(self, house_values):
        """
        Function to determine the maximum amount of money that can be robbed without robbing two adjacent houses.
        :param house_values: List of integers representing the value of money in each house.
        :return: Maximum money that can be robbed.
        """
        num_houses = len(house_values)

        # Handle edge cases where there are fewer than three houses
        if num_houses == 1:
            return house_values[0]
        if num_houses == 2:
            return max(house_values)

        # Initialize variables for the dynamic programming approach
        # When the first house is picked
        max_sum_two_houses_ago = house_values[0]  # Maximum money robbed up to two houses ago
        max_sum_previous_house = max(house_values[0], house_values[1])  # Maximum money robbed up to the previous house

        # When the first house is not picked
        max_sum_two_houses_ago_no_first = 0  # Maximum money robbed up to two houses ago, excluding the first house
        max_sum_previous_house_no_first = house_values[1]  # Maximum money robbed up to the previous house, excluding the first house

        overall_max_sum = 0  # Variable to store the global maximum

        # Loop through houses starting from the third house (index 2)
        for current_index in range(2, num_houses):
            if current_index == num_houses - 1:
                # For the last house, consider only when the first house is picked
                current_max_sum = max(max_sum_two_houses_ago, max_sum_previous_house)
            else:
                # Calculate the maximum sum when the current house is robbed
                current_max_sum = max(house_values[current_index] + max_sum_two_houses_ago, max_sum_previous_house)

            # Calculate the maximum sum when the first house is not picked
            current_max_sum_no_first = max(house_values[current_index] + max_sum_two_houses_ago_no_first, max_sum_previous_house_no_first)

            # Update the values for the next iteration
            max_sum_two_houses_ago = max_sum_previous_house
            max_sum_previous_house = current_max_sum

            max_sum_two_houses_ago_no_first = max_sum_previous_house_no_first
            max_sum_previous_house_no_first = current_max_sum_no_first

            # Update the overall maximum
            overall_max_sum = max(current_max_sum, current_max_sum_no_first)

        return overall_max_sum
