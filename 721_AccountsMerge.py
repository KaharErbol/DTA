class UnionFind:
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.rank = [1] * N
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_hash = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email_hash:
                    uf.union(i, email_hash[e])
                else:
                    email_hash[e] = i
        
        ans = {}

        for e, a_idx in email_hash.items():
            leader = uf.find(a_idx)
            if leader not in ans:
                ans[leader] = []
            ans[leader].append(e)

        res = []
        for idx, emails in ans.items():
            acc_name = accounts[idx][0]
            res.append([acc_name] + sorted(emails))
        
        return res


