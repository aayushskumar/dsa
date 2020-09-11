
""" 
Algorithm:
    
    BFS(v):
        for each v in G:
            set v.visited = False
        Create a queue = []
        append v into queue
        set v.visited = True
        while queue is not empty:
            remove head v of queue
            for each neighbour u in G.adj[v]:
                if u.visited == False:
                    BFS(u)
    
"""

""" 
Time Complexity - O(V+E) where V is no. of vertices and E is no. of edges 
Auxilary Space- O(V)
"""

from collections import defaultdict

class Bfs:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,s,d):
        self.graph[s].append(d)
        
    def bfs(self,v):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(v)
        visited[v] = True
        while queue:
            v = queue.pop(0)
            print(v, end=" ")
            for u in self.graph[v]:
                if visited[u] == False:
                    queue.append(u)
                    visited[u] = True

if __name__ == '__main__':
    g = Bfs()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)
    
    print("BFS starting from vertex 2: ")
    g.bfs(2) # Output of code- 2 0 3 1