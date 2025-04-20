import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # Initialize adjacency matrix with infinity
        self.graph = [[0 if i == j else float('inf') 
                      for j in range(vertices)] 
                      for i in range(vertices)]
    
    def add_edge(self, u, v, w):
        # Add edge to undirected graph
        self.graph[u][v] = w
        self.graph[v][u] = w
    
    def min_key(self, key, mst_set):
        # Find vertex with minimum key value not yet included in MST
        min_val = float('inf')
        min_index = -1
        
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index
    
    def prim_mst(self):
        # Array to store constructed MST
        parent = [None] * self.V
        # Key values to pick minimum weight edge
        key = [float('inf')] * self.V
        # Track vertices included in MST
        mst_set = [False] * self.V
        
        # Start with first vertex
        key[0] = 0
        parent[0] = -1  # First node is root
        
        # MST will have V vertices
        for count in range(self.V):
            # Pick vertex with minimum key value
            u = self.min_key(key, mst_set)
            
            # Add vertex to MST
            mst_set[u] = True
            
            # Update key values and parent for adjacent vertices
            for v in range(self.V):
                if (self.graph[u][v] > 0 and 
                    not mst_set[v] and 
                    self.graph[u][v] < key[v]):
                    key[v] = self.graph[u][v]
                    parent[v] = u
        
        # Print the MST
        print("Edges in the Minimum Spanning Tree:")
        total_weight = 0
        for i in range(1, self.V):
            print(f"{parent[i]} -- {i} == {self.graph[i][parent[i]]}")
            total_weight += self.graph[i][parent[i]]
        print(f"Total weight of MST: {total_weight}")
        return parent

# Example usage
if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = Graph(5)
    
    # Add edges (u, v, weight)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)
    
    # Find MST using Prim's algorithm
    g.prim_mst()