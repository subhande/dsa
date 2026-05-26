# Prefix Sum



-> Sum(i,j) = PrefixSum(j) - PrefixSum(i-1)
-> PrefixSum(j) - PrefixSum(i-1) = k
-> PrefixSum(j) - k = PrefixSum(i-1)


[1,2,3], k = 3


PrefixSum = [1, 3, 6]

j = 0, freq = {0:1} | 1 - 3 = -2 | freq = {0:1, -2:1}
j = 1, freq = {0:1, -2:1} | 3 - 3 = 0 | freq = {0:1, -2:1, 3:1} | count = 1
j = 2, freq = {0:2, -2:1, 3:1} | 6 - 3 = 3 | freq = {0:2, -2:1, 3:1, 6:1} | count = 2


# HashMap Approach
- Initialize a HashMap to store the frequency of prefix sums.
