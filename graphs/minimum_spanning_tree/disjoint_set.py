# Disjoint Set
# Union Fuid
# Helpful in Dynamic Graph
# https://takeuforward.org/plus/dsa/graph/minimum-spanning-tree/disjoint-set-


class DisjointSet:
     # Constructor
    def __init__(self, n):
        # Resize the arrays
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    # Helper function to find ultimate
    # parent along with path compression
    def findUPar(self, node):
        # Base Case
        if node == self.parent[node]:
            return node

        # Backtracking step for path compression
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]


    def find(self, u: int, v: int) -> bool:
        # Return true if both have same ultimate parent
        return self.findUPar(u) == self.findUPar(v)

    # Function to perform union of
    # two nodes based on ranks
    def unionByRank(self, u: int, v: int) -> None:
        # Get the ultimate parents of both nodes
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        # Return if nodes already belong to the same component
        if ulp_u == ulp_v:
            return

        # Otherwise, join the node to the other
        # node having higher ranks among the two
        if self.rank[ulp_u] < self.rank[ulp_v]:
            # Update the parent
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            # Update the parent
            self.parent[ulp_v] = ulp_u
        else:
            # Update the parent
            self.parent[ulp_v] = ulp_u
            # Update the rank
            self.rank[ulp_u] += 1


    # Function to perform union of
    # two nodes based on sizes
    def unionBySize(self, u, v):
       # Get the ultimate parents of both nodes
       ulp_u = self.findUPar(u)
       ulp_v = self.findUPar(v)

       # Return if nodes already belong to the same component
       if ulp_u == ulp_v:
           return

       # Otherwise, join the node belonging to the smaller
       # component to the node belonging to bigger component
       if self.size[ulp_u] < self.size[ulp_v]:
           # Update the parent
           self.parent[ulp_u] = ulp_v
           # Update the size
           self.size[ulp_v] += self.size[ulp_u]
       else:
           # Update the parent
           self.parent[ulp_v] = ulp_u
           # Update the size
           self.size[ulp_u] += self.size[ulp_v]
