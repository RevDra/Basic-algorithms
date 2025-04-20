class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]  # Adjacency matrix
    
    def add_edge(self, u, v):
        """Add an undirected edge"""
        self.graph[u][v] = 1
        self.graph[v][u] = 1
    
    def is_safe(self, v, pos, path):
        """Check if vertex v can be added at position pos in path"""
        # Check if this vertex is adjacent to the previous vertex
        if self.graph[path[pos-1]][v] == 0:
            return False
        
        # Check if the vertex has already been included
        if v in path[:pos]:
            return False
        
        return True
    
    def hamilton_util(self, path, pos, find_circuit):
        """Recursive utility function to find Hamiltonian Path/Circuit"""
        # Base case: if all vertices are included
        if pos == self.V:
            # For circuit: check if there's an edge from last to first vertex
            if find_circuit:
                return self.graph[path[pos-1]][path[0]] == 1
            return True
        
        # Try different vertices as next candidates
        for v in range(self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                
                if self.hamilton_util(path, pos + 1, find_circuit):
                    return True
                
                # Backtrack
                path[pos] = -1
        
        return False
    
    def find_hamilton_circuit(self):
        """Find a Hamiltonian Circuit if it exists"""
        # Initialize path with -1 (unvisited)
        path = [-1] * self.V
        
        # Start with vertex 0
        path[0] = 0
        
        if not self.hamilton_util(path, 1, True):
            return "No Hamiltonian Circuit exists"
        
        return f"Hamiltonian Circuit: {' -> '.join(map(str, path + [path[0]]))}"
    
    def find_hamilton_path(self):
        """Find a Hamiltonian Path if it exists"""
        # Initialize path with -1 (unvisited)
        path = [-1] * self.V
        
        # Try each vertex as starting point
        for start in range(self.V):
            path[0] = start
            if self.hamilton_util(path, 1, False):
                return f"Hamiltonian Path: {' -> '.join(map(str, path))}"
        
        return "No Hamiltonian Path exists"

# Example usage
def main():
    # Example 1: Graph with Hamiltonian Circuit
    g1 = Graph(5)
    g1.add_edge(0, 1)
    g1.add_edge(0, 3)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(1, 4)
    g1.add_edge(2, 4)
    g1.add_edge(3, 4)
    print("Graph 1:")
    print(g1.find_hamilton_circuit())
    print(g1.find_hamilton_path())
    
    # Example 2: Graph with Hamiltonian Path but no Circuit
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    print("\nGraph 2:")
    print(g2.find_hamilton_circuit())
    print(g2.find_hamilton_path())

if __name__ == "__main__":
    main()