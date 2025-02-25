class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph=defaultdict(set)
        
        visited=set()
        def dfs(u,v,visited):
            if u==v:
                return True
            
            visited.add(u)
            for n in graph[u]:
                if n not in visited and dfs(n,v,visited):
                    return True
            return False
        
        for u,v in edges:
            if u in graph and v in graph and dfs(u,v,visited):
                return [u,v]
            
            visited=set()
            graph[u].add(v)
            graph[v].add(u)
            
            