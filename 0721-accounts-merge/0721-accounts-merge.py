class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
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
        mailToAcc = {}
        for i,acc in enumerate(accounts):
            for email in acc[1:]:
                if email in mailToAcc:
                    uf.union(i, mailToAcc[email])
                else:
                    mailToAcc[email] = i
        print(uf.par)
        print(mailToAcc)
        # idx => mail
        idxToMail = defaultdict(list)
        for mail,idx in mailToAcc.items():
            rootIdx =  uf.find(idx)
            idxToMail[rootIdx].append(mail)
        print(idxToMail)
        res = []
        for idx, mails in idxToMail.items():
            name = accounts[idx][0]
            res.append( [name] + sorted(mails) )
        return res


        # def dfs(graph,email,visited):
        #     if email in visited:
        #         return
        #     visited.add(email)
        #     for nei in graph[email]:
        #         dfs(graph,nei,visited)
        #     self.res.append(email)

        # graph = defaultdict(set)
        # for acc in accounts:
        #     for email in acc[1:]:
        #         graph[acc[1]].add(email)
        #         graph[email].add(acc[1])
        # print(graph)
        # visited = set()
        # ans = []
        # for acc in accounts:
        #     name = acc[0]
        #     for email in acc[1:]:
        #         if email not in visited:
        #             self.res = []
        #             dfs(graph,email,visited)
        #             ans.append([name]+sorted(self.res))
        # return ans
