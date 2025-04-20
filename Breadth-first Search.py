from collections import deque

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
    
    def bfs_traversal(self, start):
        """Perform BFS traversal starting from given vertex"""
        if start not in self.graph:
            return "Starting vertex not in graph"
        
        visited = set()
        queue = deque([start])
        traversal = []
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                # Add all unvisited neighbors to queue
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return f"BFS Traversal: {' -> '.join(map(str, traversal))}"
    
    def bfs_shortest_path(self, start, end):
        """Find shortest path between start and end vertices using BFS"""
        if start not in self.graph or end not in self.graph:
            return "Start or end vertex not in graph"
        
        visited = set()
        queue = deque([(start, [start])])  # (vertex, path)
        
        while queue:
            vertex, path = queue.popleft()
            
            if vertex == end:
                return f"Shortest path: {' -> '.join(map(str, path))}"
            
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        queue.append((neighbor, new_path))
        
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
    
    # BFS traversal starting from vertex 0
    print("\n" + g.bfs_traversal(0))
    
    # Find shortest path between vertices
    print(g.bfs_shortest_path(0, 4))
    print(g.bfs_shortest_path(0, 5))
    print(g.bfs_shortest_path(2, 5))

if __name__ == "__main__":
    main()