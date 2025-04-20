import sys
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        # Increase recursion limit (Solution 1)
        sys.setrecursionlimit(10000)  # Be cautious with this
    
    # Recursive approach with increased limit
    def preorder_recursive(self):
        if self.root is None:
            return []
        result = []
        def preorder(node):
            if node:
                result.append(node.value)
                preorder(node.left)
                preorder(node.right)
        preorder(self.root)
        return result
    
    # Iterative approach using stack (Solution 2)
    def preorder_iterative(self):
        if self.root is None:
            return []
        
        result = []
        stack = [self.root]
        
        while stack:
            node = stack.pop()
            if node:
                result.append(node.value)
                # Push right first so left is processed first
                stack.append(node.right)
                stack.append(node.left)
        
        return result
    
    # Iterative inorder traversal
    def inorder_iterative(self):
        if self.root is None:
            return []
        
        result = []
        stack = []
        current = self.root
        
        while stack or current:
            # Reach the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.value)
            current = current.right
        
        return result
    
    # Iterative postorder traversal using two stacks
    def postorder_iterative(self):
        if self.root is None:
            return []
        
        result = []
        stack1 = [self.root]
        stack2 = []
        
        while stack1:
            node = stack1.pop()
            if node:
                stack2.append(node)
                stack1.append(node.left)
                stack1.append(node.right)
        
        while stack2:
            result.append(stack2.pop().value)
        
        return result

# Function to create a deep tree for testing
def create_deep_tree(depth):
    tree = BinaryTree()
    current = Node(0)
    tree.root = current
    
    for i in range(1, depth):
        current.left = Node(i)
        current = current.left
    
    return tree

# Example usage
def main():
    # Test with a normal tree
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    
    print("Normal tree traversals:")
    print(f"Preorder (recursive): {tree.preorder_recursive()}")
    print(f"Preorder (iterative): {tree.preorder_iterative()}")
    print(f"Inorder (iterative):  {tree.inorder_iterative()}")
    print(f"Postorder (iterative): {tree.postorder_iterative()}")
    
    # Test with a deep tree
    deep_tree = create_deep_tree(1500)  # Depth > 1000 to test recursion limit
    print("\nDeep tree traversals:")
    try:
        print(f"Preorder (recursive): First 10 elements: {deep_tree.preorder_recursive()[:10]}...")
    except RecursionError:
        print("Preorder (recursive): RecursionError occurred")
    print(f"Preorder (iterative): First 10 elements: {deep_tree.preorder_iterative()[:10]}...")
    print(f"Inorder (iterative):  First 10 elements: {deep_tree.inorder_iterative()[:10]}...")
    print(f"Postorder (iterative): First 10 elements: {deep_tree.postorder_iterative()[:10]}...")

if __name__ == "__main__":
    main()