
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit=[0]*numCourses
        graph=defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
        
        def dfs(node):
            if visit[node]==1:
                return False
            if visit[node]==2:
                return True
            
            visit[node]=1
            for c in graph[node]:
                if not dfs(c):
                    return False
            
            visit[node]=2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

