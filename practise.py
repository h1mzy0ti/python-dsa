arr = [2, 1, 5, 1, 3, 2,23]
k = 3

def sliding_window(arr,k):
    n = len(arr)
    if n < k:
        return -1
    
    #step1
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k,n):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum,window_sum)

    return max_sum
print(sliding_window(arr,k))
