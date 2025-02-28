def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return -1  

    # step 1:
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Step 2:
    for i in range(k, n):
        window_sum = window_sum - arr[i - k] + arr[i]  # Remove old, add new
        max_sum = max(max_sum, window_sum)  

    return max_sum


arr = [2, 1, 5, 1, 3, 2,23]
k = 3
print(max_sum_subarray(arr, k))  
