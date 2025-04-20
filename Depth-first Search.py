class Graph:
    def __init__(self):
        # Using adjacency list representation with dictionary
        self.graph = {}
    
    def add_edge(self, u, v):
        """Add an undirected edge"""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # Remove this line for directed graph
    
    def dfs_traversal(self, start):
        """Perform DFS traversal starting from given vertex"""
        if start not in self.graph:
            return "Starting vertex not in graph"
        
        visited = set()
        traversal = []
        
        def dfs(vertex):
            visited.add(vertex)
            traversal.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(start)
        return f"DFS Traversal: {' -> '.join(map(str, traversal))}"
    
    def dfs_path(self, start, end):
        """Find a path between start and end vertices using DFS"""
        if start not in self.graph or end not in self.graph:
            return "Start or end vertex not in graph"
        
        visited = set()
        path = []
        
        def dfs_path_util(vertex):
            visited.add(vertex)
            path.append(vertex)
            
            if vertex == end:
                return True
                
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs_path_util(neighbor):
                        return True
            
            path.pop()  # Backtrack
            return False
        
        if dfs_path_util(start):
            return f"Path found: {' -> '.join(map(str, path))}"
        return "No path exists between start and end vertices"

# Example usage
def main():
    g = Graph()
    
    # Add edges to create a sample graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    
    print("Graph adjacency list:")
    for vertex in g.graph:
        print(f"{vertex}: {g.graph[vertex]}")
    
    # DFS traversal starting from vertex 0
    print("\n" + g.dfs_traversal(0))
    
    # Find paths between vertices
    print(g.dfs_path(0, 4))
    print(g.dfs_path(0, 5))
    print(g.dfs_path(2, 5))

if __name__ == "__main__":
    main()