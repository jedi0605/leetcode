class Unifind:
    def __init__(self,n):
        self.par = []
        for i in range(n):
            self.par.append(i)
            i+=1
        self.rank = [1]*n

    def find(self, x):
        # find par
        while x!= self.par[x]:
            x = self.par[x]
        return x        

    def union(self,x1,x2):
        p1,p2 = self.find(x1),self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2]+=self.rank[p1]
        return True    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = Unifind(len(accounts))
        mail2Idx = {}

        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in mail2Idx:
                    uf.union(i, mail2Idx[email])
                else:
                    mail2Idx[email] = i
        
        idxAndMails = defaultdict(list)
        for mail,idx in mail2Idx.items():
            par = uf.find(idx)
            idxAndMails[par].append(mail)
        print(idxAndMails)

        res = []
        for idx, mails in idxAndMails.items():
            # print(mails)
            name = accounts[idx][0]
            tmp = [name] + sorted(mails)
            print(tmp)
            res.append(tmp)
        return res