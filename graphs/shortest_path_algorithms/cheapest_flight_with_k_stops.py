# Cheapest Flight With K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# https://takeuforward.org/plus/dsa/graph/shortest-path-algorithms/cheapest-flight-within-k-stops


from typing import List
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for flight in flights:
            adj[flight[0]].append([flight[1], flight[2]])
        # print(adj)
        INF = float("inf")
        cost = [INF] * n
        cost[src] = 0
        minHeap = [(0, src, 0)]

        while minHeap:
            c, node, stop = heapq.heappop(minHeap)

            if stop > k:
                continue

            for neighbor, n_cost in adj[node]:
                # print(node, adj[node], neighbor, n_cost, cost)
                if cost[node] + n_cost < cost[neighbor] and stop <= k:
                    cost[neighbor] = cost[node] + n_cost
                    heapq.heappush(minHeap, (cost[neighbor], neighbor, stop+1))

        return cost[dst] if cost[dst] != INF else -1


if __name__ == '__main__':

    sol = Solution()

    # Test 1
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    # Output: 700
    print(sol.findCheapestPrice(n, flights, src, dst, k))

    # Test 2
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    # Output: 500
    print(sol.findCheapestPrice(n, flights, src, dst, k))

    # # Test 3
    # n = 5
    # flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
    # src = 0
    # dst = 2
    # k = 2
    # # Output: 7
    # print(sol.findCheapestPrice(n, flights, src, dst, k))
