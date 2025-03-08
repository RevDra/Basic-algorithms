def binary_search_iterative(arr, target):
    """
    Iterative implementation of binary search.
    Args:
        arr: Sorted list of comparable elements
        target: Element to find
    Returns:
        Index of target if found, -1 if not found
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Found the target
        if arr[mid] == target:
            return mid
        
        # Target is in right half
        elif arr[mid] < target:
            left = mid + 1
            
        # Target is in left half
        else:
            right = mid - 1
            
    return -1  # Target not found

def binary_search_recursive(arr, target, left=None, right=None):
    """
    Recursive implementation of binary search.
    Args:
        arr: Sorted list of comparable elements
        target: Element to find
        left: Left boundary (default None for initial call)
        right: Right boundary (default None for initial call)
    Returns:
        Index of target if found, -1 if not found
    """
    # Initialize boundaries on first call
    if left is None and right is None:
        left = 0
        right = len(arr) - 1
    
    # Base case: search space exhausted
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    # Found the target
    if arr[mid] == target:
        return mid
    
    # Recursive cases
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage
if __name__ == "__main__":
    # Test array (must be sorted for binary search to work)
    numbers = [2, 3, 4, 10, 40, 50, 60, 70]
    
    # Test cases
    test_values = [4, 70, 5, 40]
    
    print("Iterative Binary Search:")
    for value in test_values:
        result = binary_search_iterative(numbers, value)
        if result != -1:
            print(f"Found {value} at index {result}")
        else:
            print(f"{value} not found in array")
            
    print("\nRecursive Binary Search:")
    for value in test_values:
        result = binary_search_recursive(numbers, value)
        if result != -1:
            print(f"Found {value} at index {result}")
        else:
            print(f"{value} not found in array")