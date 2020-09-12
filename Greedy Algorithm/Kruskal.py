
""" 
Algorithm:
    
    KruskalsAlgo(G):
        A = phi
        for each vetex v in G.V:
            MAKE-SET(v)
        for each edge (u,v) belongs to G.E sorted in increasing order of weight(u,v):
            if FIND-SET(u) != FIND-SET(v):
                A = A U {(u,v)}
                Union(u,v)
                
        return A
    
"""

""" 
Time Complexity - O(ElogE) where V is no. of vertices and E is no. of edges
"""


class KruskalsALgo:
    def __init__(self,v):
        self.V = v
        self.graph = []
        
    # Method to add source, destination and weight
    def addEdge(self,s,d,w):
        self.graph.append([s,d,w])
        
    # Method to find set of element i
    # uses path compression technique
    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])
    
    # Method that does union of two sets x and y
    # uses union by rank
    def union(self,parent,rank,x,y):
        xParent = self.find(parent, x)
        yParent = self.find(parent, y)
        if rank[xParent] < rank[yParent]:
            parent[xParent] = yParent
        elif rank[xParent] > rank[yParent]:
            parent[yParent] = xParent
        else:
            parent[yParent] = xParent
            rank[xParent] += 1
        
    # Main metod to construct MST using Kruskal's algorithm
    def kruskalsAlgo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key = lambda item: item[2])
        parent = []
        rank = []
        
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u,v,w])
                self.union(parent,rank,x,y)
                
        # Prints the solution
        for u,v,w in result:
            print("%d - %d: %d"%(u,v,w))
            
        """ Output of code:
            1 - 2: 2
            2 - 5: 2
            2 - 3: 3
            3 - 4: 3
            0 - 1: 4 """
        

if __name__ == '__main__':
    g = KruskalsALgo(6)
    g.addEdge(0, 1, 4)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 2)
    g.addEdge(1, 0, 4)
    g.addEdge(2, 0, 4)
    g.addEdge(2, 1, 2)
    g.addEdge(2, 3, 3)
    g.addEdge(2, 5, 2)
    g.addEdge(2, 4, 4)
    g.addEdge(3, 2, 3)
    g.addEdge(3, 4, 3)
    g.addEdge(4, 2, 4)
    g.addEdge(4, 3, 3)
    g.addEdge(5, 2, 2)
    g.addEdge(5, 4, 3)
    
    g.kruskalsAlgo()