def solve():
  
    N, K = 4, 2
    A = [4, 2, 6, 2, 3]    
    expected_value = 0.0
    total_subsets = 2 ** N    
    # Iterate through all possible subsets using bitmask
    for mask in range(total_subsets):
        subset_sum = 0
        for i in range(N):
            if mask & (1 << i):
                subset_sum += A[i]
        
        prob = 1.0 / total_subsets
        expected_value += (subset_sum ** K) * prob
    
    # Round to 2 decimal places
    result = round(expected_value, 2)
    print(f"{result:.2f}")
solve()
