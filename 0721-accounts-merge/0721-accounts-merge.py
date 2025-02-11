class Solution:    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def dfs(graph,email,visited):
            visited.add(email)
            for nei in graph[email]:
                if nei not in visited:
                    dfs(graph,nei,visited)
            self.res.append(email)

        graph = defaultdict(set)
        for acc in accounts:
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
        
        visited = set()
        ans = []
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in visited:
                    self.res = []
                    dfs(graph,email,visited)
                    ans.append([name]+sorted(self.res))
        return ans