class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Insert a value into the BST"""
        if not self.root:
            self.root = Node(value)
            return True
        
        def _insert_recursive(node, value):
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return True
                return _insert_recursive(node.left, value)
            elif value > node.value:
                if node.right is None:
                    node.right = Node(value)
                    return True
                return _insert_recursive(node.right, value)
            else:
                return False  # Value already exists
        
        return _insert_recursive(self.root, value)
    
    def search(self, value):
        """Search for a value in the BST"""
        def _search_recursive(node, value):
            if node is None:
                return False
            if node.value == value:
                return True
            elif value < node.value:
                return _search_recursive(node.left, value)
            else:
                return _search_recursive(node.right, value)
        
        return _search_recursive(self.root, value)
    
    # Helper method to print tree (inorder traversal)
    def inorder(self):
        """Return inorder traversal of the tree"""
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result
    
    # Iterative versions for comparison
    def insert_iterative(self, value):
        """Iterative insertion into BST"""
        new_node = Node(value)
        
        if not self.root:
            self.root = new_node
            return True
        
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right
            else:
                return False  # Value already exists
    
    def search_iterative(self, value):
        """Iterative search in BST"""
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

# Example usage with testing
def main():
    bst = BinarySearchTree()
    
    # Test values
    values = [50, 30, 70, 20, 40, 60, 80, 10]
    
    # Insert values (recursive)
    print("Inserting values recursively:")
    for val in values:
        success = bst.insert(val)
        print(f"Inserted {val}: {'Success' if success else 'Failed (duplicate)'}")
    
    # Print tree
    print(f"\nInorder traversal: {bst.inorder()}")
    
    # Search tests
    test_values = [40, 90, 20, 50]
    print("\nSearching values:")
    for val in test_values:
        found = bst.search(val)
        print(f"Search {val}: {'Found' if found else 'Not found'}")
    
    # Test iterative insertion
    bst_iter = BinarySearchTree()
    print("\nInserting values iteratively:")
    for val in values:
        success = bst_iter.insert_iterative(val)
        print(f"Inserted {val}: {'Success' if success else 'Failed (duplicate)'}")
    
    # Test iterative search
    print("\nSearching values (iterative):")
    for val in test_values:
        found = bst_iter.search_iterative(val)
        print(f"Search {val}: {'Found' if found else 'Not found'}")

if __name__ == "__main__":
    main()