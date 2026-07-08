# Number of People Aware of a Secret

from collections import deque


# Approach 1: Brute Force | TLE
# Time Complexity: O(2^n) | Space Complexity: O(n)
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        queue = deque()

        # (ele, day_no, known_since)
        count = 1
        queue.append((f"a{count}", 1, 0))

        while queue:
            ele, day_no, known_since = queue.popleft()

            if day_no > n:
                continue

            if known_since == forget:
                count -= 1
                continue

            queue.append((ele, day_no + 1, known_since + 1))

            if known_since >= delay:
                count = (count + 1) % (10**9 + 7)
                queue.append((f"a{count}", day_no, 0))

        return count


# Approach 2: Deque + Simulation
# Time Complexity: O(n) | Space Complexity: O(n)
class Solution2:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        know, share = deque([(1, 1)]), deque([])
        know_cnt, share_cnt = 1, 0
        # Day 1: person A learns it, sits in `know` (not yet allowed to share)

        for i in range(2, n + 1):
            # --- Transition 1: know -> share ---
            # A group that learned on day `know[0][0]` becomes active exactly
            # `delay` days later. So if today (i) equals know[0][0] + delay,
            # i.e. know[0][0] == i - delay, that whole group starts sharing NOW.
            if know and know[0][0] == i - delay:
                know_cnt -= know[0][1]
                share_cnt += know[0][1]
                share.append(know[0])
                know.popleft()

            # --- Transition 2: share -> gone (forgotten) ---
            # A group that learned on day `share[0][0]` forgets exactly
            # `forget` days later: share[0][0] == i - forget.
            # They just leave -- no destination deque, they're done.
            if share and share[0][0] == i - forget:
                share_cnt -= share[0][1]
                share.popleft()

            # --- New people learn today ---
            # Everyone currently in `share` spreads to exactly 1 new person
            # each, so share_cnt new people learn it today. They start life
            # in `know` (their own delay clock starts now).
            if share:
                know_cnt += share_cnt
                know.append((i, share_cnt))

        return (know_cnt + share_cnt) % (10**9 + 7)


## Approach 3: Dynamic Programming
# TODO: Implement the DP approach for the problem of counting the number of people aware of a secret. This approach will involve creating a DP array to keep track of the number of people who learn the secret on each day, and then using that information to calculate the total number of people aware of the secret by the end of day n.
