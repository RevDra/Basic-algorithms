class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list
    
    def add_edge(self, u, v):
        """Add an undirected edge"""
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def get_degrees(self):
        """Return list of degrees for each vertex"""
        return [len(adj) for adj in self.graph]
    
    def is_connected(self):
        """Check if graph is connected using DFS"""
        visited = [False] * self.V
        start_vertex = 0
        
        # Find a vertex with non-zero degree
        for i in range(self.V):
            if len(self.graph[i]) > 0:
                start_vertex = i
                break
        
        def dfs(v):
            visited[v] = True
            for u in self.graph[v]:
                if not visited[u]:
                    dfs(u)
        
        dfs(start_vertex)
        # Check if all vertices with non-zero degree are visited
        for i in range(self.V):
            if not visited[i] and len(self.graph[i]) > 0:
                return False
        return True
    
    def has_euler_circuit(self):
        """Check if graph has Euler Circuit"""
        if not self.is_connected():
            return False
        
        # All vertices must have even degree
        degrees = self.get_degrees()
        return all(deg % 2 == 0 for deg in degrees)
    
    def has_euler_path(self):
        """Check if graph has Euler Path"""
        if not self.is_connected():
            return False
        
        # Must have either 0 or 2 vertices with odd degree
        degrees = self.get_degrees()
        odd_count = sum(1 for deg in degrees if deg % 2 == 1)
        return odd_count == 0 or odd_count == 2
    
    def find_euler_path_or_circuit(self):
        """Find Euler Circuit if exists, otherwise Euler Path"""
        if not self.has_euler_path():
            return "No Euler Path or Circuit exists"
        
        # Create a copy of adjacency list
        graph_copy = [list(adj) for adj in self.graph]
        result = []
        
        # Find starting vertex (vertex with odd degree if exists)
        degrees = self.get_degrees()
        start = 0
        for i in range(self.V):
            if degrees[i] % 2 == 1:
                start = i
                break
        
        def dfs(u):
            while graph_copy[u]:
                v = graph_copy[u].pop()
                # Remove reverse edge
                graph_copy[v].remove(u)
                dfs(v)
            result.append(u)
        
        dfs(start)
        result.reverse()  # Reverse to get correct order
        
        # Check if it's a circuit
        if self.has_euler_circuit():
            return f"Euler Circuit: {' -> '.join(map(str, result + [result[0]]))}"
        return f"Euler Path: {' -> '.join(map(str, result))}"

# Example usage
def main():
    # Example 1: Graph with Euler Circuit
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(0, 3)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    print("Graph 1:")
    print(g1.find_euler_path_or_circuit())
    
    # Example 2: Graph with Euler Path
    g2 = Graph(5)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(3, 4)
    g2.add_edge(4, 1)
    print("\nGraph 2:")
    print(g2.find_euler_path_or_circuit())

if __name__ == "__main__":
    main()