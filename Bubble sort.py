def bubble_sort(arr):
    """
    Sorts an array in ascending order using the bubble sort algorithm.
    Args:
        arr: List of comparable elements (numbers or strings)
    Returns:
        The sorted array
    """
    n = len(arr)
    
    # Outer loop for number of passes
    for i in range(n):
        # Flag to optimize by checking if any swaps occurred
        swapped = False
        
        # Inner loop for comparing adjacent elements
        # We subtract i because after each pass, the last i elements are already sorted
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr

# Example usage
if __name__ == "__main__":
    # Test with numbers
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", numbers)
    sorted_numbers = bubble_sort(numbers)
    print("Sorted array:", sorted_numbers)
    
    # Test with strings
    words = ["banana", "apple", "cherry", "date"]
    print("\nOriginal array:", words)
    sorted_words = bubble_sort(words)
    print("Sorted array:", sorted_words)