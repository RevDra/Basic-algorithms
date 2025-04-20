class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []    # List to store graph edges
        
    def add_edge(self, u, v, w):
        # Add edge to graph with vertices u, v and weight w
        self.graph.append([u, v, w])
    
    # Find function for union-find with path compression
    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    # Union function for union-find
    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)
        
        # Attach smaller rank tree under root of higher rank tree
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1
    
    def kruskal_mst(self):
        result = []  # Store the resultant MST
        i = 0        # Index for sorted edges
        e = 0        # Index for result[]
        
        # Sort all edges by weight
        self.graph = sorted(self.graph, key=lambda item: item[2])
        
        parent = []
        rank = []
        
        # Initialize parent and rank arrays
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        # Process all edges
        while e < self.V - 1 and i < len(self.graph):
            # Pick the smallest edge
            u, v, w = self.graph[i]
            i += 1
            
            x = self.find(parent, u)
            y = self.find(parent, v)
            
            # If including this edge doesn't create a cycle
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        
        # Print the MST
        print("Edges in the Minimum Spanning Tree:")
        total_weight = 0
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")
            total_weight += weight
        print(f"Total weight of MST: {total_weight}")
        return result

# Example usage
if __name__ == "__main__":
    # Create a graph with 4 vertices
    g = Graph(4)
    
    # Add edges (u, v, weight)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    
    # Find MST using Kruskal's algorithm
    g.kruskal_mst()