def gaussian_elimination(A, b):
    """
    Solve system of linear equations Ax = b using Gaussian Elimination
    A: coefficient matrix (n x n)
    b: constant vector (n x 1)
    Returns: solution vector x
    """
    n = len(b)
    # Create augmented matrix [A|b]
    augmented = [A[i] + [b[i]] for i in range(n)]
    
    # Forward Elimination
    for i in range(n):
        # Find pivot
        pivot = augmented[i][i]
        if abs(pivot) < 1e-10:  # Check for zero pivot
            raise ValueError("Matrix is singular or nearly singular")
            
        # Make pivot 1 by dividing row by pivot
        for j in range(i, n + 1):
            augmented[i][j] /= pivot
            
        # Eliminate column
        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(i, n + 1):
                    augmented[k][j] -= factor * augmented[i][j]
    
    # Extract solution
    x = [augmented[i][n] for i in range(n)]
    
    # Verify solution (optional)
    print("Solution vector x:", x)
    print("Verification (Ax should equal b):")
    for i in range(n):
        row_sum = sum(A[i][j] * x[j] for j in range(n))
        print(f"Equation {i+1}: {row_sum} ≈ {b[i]}")
    
    return x

# Example usage with error handling
def main():
    try:
        # Example system:
        # 2x + y - z = 8
        # -3x - y + 2z = -11
        # -2x + y + 2z = -3
        A = [
            [2, 1, -1],
            [-3, -1, 2],
            [-2, 1, 2]
        ]
        b = [8, -11, -3]
        
        print("Coefficient matrix A:")
        for row in A:
            print(row)
        print("Constant vector b:", b)
        
        solution = gaussian_elimination(A, b)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()