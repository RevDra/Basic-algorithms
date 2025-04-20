def selection_sort(arr):
    """
    Sort an array using the selection sort algorithm
    Args:
        arr: List of comparable elements
    Returns:
        Sorted list (in ascending order)
    """
    # Make a copy of the input array to avoid modifying the original
    arr = arr.copy()
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element of unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Alternative implementation with step-by-step printing
def selection_sort_with_steps(arr):
    """
    Sort an array using selection sort and print steps
    Args:
        arr: List of comparable elements
    Returns:
        Sorted list (in ascending order)
    """
    arr = arr.copy()
    n = len(arr)
    
    print(f"Initial array: {arr}")
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap and print step
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"Step {i+1}: After swapping {arr[i]} and {arr[min_idx]}: {arr}")
    
    print(f"Sorted array: {arr}")
    return arr

# Example usage
def main():
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 1, 2, 2]
    ]
    
    print("Simple Selection Sort:")
    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = selection_sort(arr)
        print(f"Original: {original}")
        print(f"Sorted:   {sorted_arr}\n")
    
    print("Selection Sort with Steps:")
    arr = [64, 34, 25, 12, 22]
    selection_sort_with_steps(arr)

if __name__ == "__main__":
    main()