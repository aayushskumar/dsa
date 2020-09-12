
""" 
Floyd Warshall solves all pair shortest path problem. It is an algorithm to find shortest distance path between all pairs of vertices in weighted graph. It works for both directed and undirected graph but it does not work for negetive cycles (where sum of edges in cycle is negetive)

Algorithm:
    
    FloydWarshall():
        V = no. of vertices
        result = create matrix of dimension V*V
        for k = 1 to V:
            for i = 1 to V:
                for j = 1 to V:
                    result[i][j] = min(result[i][j], (result[i][k] + result[k][j]) )
                    
        return result
"""

""" 
Time Complexity - O(V^3)
Auxilary Space- O(V^2)
"""


class FloydWarshall:
    def __init__(self):
        self.V = 4
        self.result = [[None for i in range(self.V)] for j in range(self.V)]
        
    # Algorithm implementation to solve all pair shortest path
    def floydWarshall(self,graph):
        for i in range(self.V):
            for j in range(self.V):
                self.result[i][j] = graph[i][j]
                
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if self.result[i][j] > (self.result[i][k] + self.result[k][j]):
                        self.result[i][j] = self.result[i][k] + self.result[k][j]
                
    # Method to print the solution
    def printGraph(self):
        for i in range(self.V):
            for j in range(self.V):
                if self.result[i][j] == INF:
                    print("INF", end = " ")
                else:
                    print(self.result[i][j], end = " ")
            print()
            
    """ Output of code:
            0 3 9 7
            2 0 6 4
            3 1 0 5
            5 3 2 0 """
                        

if __name__ == '__main__':
    graph = FloydWarshall()
    INF = 99999
    G = [[0,3,INF,10],
             [2,0,INF,4],
             [INF,1,0,INF],
             [INF,INF,2,0]]
    
    graph.floydWarshall(G)
    graph.printGraph()