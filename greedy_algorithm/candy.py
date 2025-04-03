# Candy

from typing import List

# Time : O(2N) | Space: O(2N)
class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)

        if n == 1:
            return 1

        left_candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left_candies[i] = left_candies[i-1]+1


        right_candies = [1] * n

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right_candies[i] = right_candies[i+1]+1

        candyCount = 0
        for i in range(n):
            candyCount += max(left_candies[i], right_candies[i])

        return candyCount


# Time : O(N) | Space: O(N)
class Solution2:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)

        if n == 1:
            return 1

        left_candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left_candies[i] = left_candies[i-1]+1


        cur = 1
        right = 1
        sum_candies = max(1, left_candies[n - 1])

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right += 1
            else:
                right = 1

            cur = max(left_candies[i], right)
            sum_candies += cur

        return sum_candies


# Time : O(N) | Space: O(N)
class Solution3:
    def candy(self, ratings: List[int]) -> int:
        # Size of the ratings array
        n = len(ratings)

        # Initialize index variable
        i = 1

        '''Initialize the total number of candies,
        starting with one candy for the first child'''
        sum = 1

        # Loop the ratings array
        while i < n:

            '''Check if the current child's rating
            is equal to the previous one'''
            if ratings[i] == ratings[i - 1]:

                '''If so, give the current child one
                more candy than the previous one'''
                sum += 1

                '''Move to the next child'''
                i += 1

                '''Skip the rest of the loop and
                move to the next iteration'''
                continue

            '''Initialize the candy count
            for increasing rating trend'''
            peak = 1

            # Loop through increasing ratings trend
            while i < n and ratings[i] > ratings[i - 1]:

                '''Increment candy count
                for increasing trend'''
                peak += 1

                '''Update the total
                number of candies'''
                sum += peak

                # Move to next
                i += 1

            '''Initialize the candy count
            for decreasing rating trend'''
            down = 1

            # Loop through decreasing ratings trend
            while i < n and ratings[i] < ratings[i - 1]:

                '''Update the total number of
                candies for decreasing trend'''
                sum += down

                # Move to next
                i += 1

                '''Increment the candy
                count for decreasing trend'''
                down += 1

            '''Check if the candy count for
            decreasing trend exceeds the peak'''
            if down > peak:
                '''Adjust the total number of
                candies to satisfy the condition'''
                sum += (down - peak)

        # Return total candies
        return sum
