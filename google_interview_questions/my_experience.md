
# Google L4 Interview Experience

# Phone Screen
- Overlapping Intervals with DNS - find maximum valid intervals

# Onsite 1

# Onsite 2
- Movie recomendation system.
Given
- Movie A - 8
- Movie B - 7
- Movie C - 6
- Movie D - 5
Relations:
- Movie A is similar to Movie B
- Movie B is similar to Movie C

Transitive relations

- Movie A is similar to Movie C

Given a movie find top n similar movies

# Onsite 3

- Unique event at timestamp T
- We have a router with different events at diff timestamps. Get Unique events at timestamp T for last N seconds.

- T      -    A
- T10s   -    B  | getCount() -> 1
- T1m20s   -  C  | getCount() -> 2
- T2m30s   -  A  | getCount() -> 3
- T3m0s   -   _  | getCount() -> 3
- T4m0s   -   B  | getCount() -> 3
- T5m0s   -   C  | getCount() -> 3
- T6m0s   -   _  | getCount() -> 2
