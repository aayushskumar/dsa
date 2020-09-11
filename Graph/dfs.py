
""" 
Algorithm:
    
    DFS(v):
        set v.visited = True
        for each neighbour u in G.adj[v]:
            if u.visited == False:
                DFS(G,u)
    
    main():
        for each v in G:
            set v.visited = False
        for each v in G:
            DFS(G,v)
"""

""" 
Time Complexity - O(V+E) where V is no. of vertices and E is no. of edges 
Auxilary Space- O(V)
"""

from collections import defaultdict

class Dfs:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,s,d):
        self.graph[s].append(d)
        
    def dfs(self,v):
        visited = [False] * (max(self.graph)+1)
        self.dfsUtil(v,visited)
        
    def dfsUtil(self,v,visited):
        visited[v] = True
        print(v, end=" ")
        for u in self.graph[v]:
            if visited[u] == False:
                self.dfsUtil(u,visited)

if __name__ == '__main__':
    g = Dfs()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)
    
    print("DFS starting from vertex 2: ")
    g.dfs(2) # Output of code- 2 0 1 3