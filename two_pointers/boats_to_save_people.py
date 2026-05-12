class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boatCount = 0
        n = len(people)
        left = 0
        right = n - 1

        while left <= right:
            boatCount += 1
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
        return boatCount
