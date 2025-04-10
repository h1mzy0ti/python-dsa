arr = [2,3,4,5,6,5]
k = 2
def sliding_window(arr,k):
    n = len(arr)
    if n < k:
        return -1
    elif n == 1:
        return arr
    

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range (k,n):
        window_sum += arr[i]
        window_sum -= arr[i - k]

        max_sum = max(window_sum,max_sum)

    return max_sum

print(sliding_window(arr,k))