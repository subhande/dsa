# Who is On Call
# https://leetcode.com/discuss/post/5670972/google-l4-onsite-by-anonymous_user-xnj8/
"""

Was asked the following question during my onsite. Ran out of time before forming a full solution, still not sure what a good approach to this would be.

Given on-call rotation schedule for multiple people by: their name, start time and end time of the rotation:

Abby 1 10
Ben 5 7
Carla 6 12
David 15 17

Your goal is to return rotation table without overlapping periods representing who is on call during that time. Return "Start time", "End time" and list of on-call people:

1 5 Abby
5 6 Abby, Ben
6 7 Abby, Ben, Carla
7 10 Abby, Carla
10 12 Carla
15 17 David


"""

import heapq
from typing import List, Any
def get_rotation_table(on_calls: List[List[Any]]) -> List[List[Any]]:

    events = []

    for start, end, name in on_calls:
        heapq.heappush(events, (start, name, 'start'))
        heapq.heappush(events, (end, name, 'end'))


    on_call = set()
    result = []

    prev_time = None

    while events:
        time, name, event_type = heapq.heappop(events)

        if prev_time != None and time != prev_time and len(on_call) > 0:
            result.append([prev_time, time, sorted(on_call)])

        prev_time = time

        if event_type == 'start':
            on_call.add(name)
        elif event_type == 'end':
            on_call.remove(name)

    return result


schedule = [[1, 10, "Abby"], [5, 7, "Ben"], [6, 12, "Carla"], [15, 17, "David"]]

print(get_rotation_table(on_calls=schedule))
# [[1, 5, ['Abby']], [5, 6, ['Abby', 'Ben']], [6, 7, ['Abby', 'Ben', 'Carla']], [7, 10, ['Abby', 'Carla']], [10, 12, ['Carla']], [15, 17, ['David']]]
