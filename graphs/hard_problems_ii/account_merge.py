# Accounts Merge
# https://takeuforward.org/plus/dsa/graph/hard-problems-ii/accounts-merge?tab=editorial
# https://leetcode.com/problems/accounts-merge/


class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]

    def findParent(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.findParent(u), self.findParent(v)
        if pu != pv:
            if self.rank[pu] < self.rank[pv]:
                self.parent[pu] = pv
            elif self.rank[pu] > self.rank[pv]:
                self.parent[pv] = pu
            else:
                self.parent[pv] = pu
                self.rank[pu] += 1

    def find(self, u, v):
        return self.findParent(u) == self.findParent(v)

class Solution:
    def accountsMerge(self, accounts):
        email_to_id = {}
        email_to_name = {}
        id = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id
                    email_to_name[email] = name
                    id += 1

        ds = DisjointSet(id)
        for account in accounts:
            for email in account[1:]:
                ds.union(email_to_id[account[1]], email_to_id[email])

        id_to_emails = {}
        for email in email_to_id:
            root = ds.findParent(email_to_id[email])
            if root not in id_to_emails:
                id_to_emails[root] = []
            id_to_emails[root].append(email)

        res = []
        for root in id_to_emails:
            res.append([email_to_name[id_to_emails[root][0]]] + sorted(id_to_emails[root]))

        return res
