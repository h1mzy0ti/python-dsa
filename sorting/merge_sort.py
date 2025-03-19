def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    m = n // 2
    L = merge_sort(arr[:m])
    R = merge_sort(arr[m:])
    
    l, r = 0, 0
    L_len, R_len = len(L), len(R)
    sorted_arr = []

    while l < L_len and r < R_len:
        if L[l] < R[r]:
            sorted_arr.append(L[l])
            l += 1
        else:
            sorted_arr.append(R[r])
            r += 1

    while l < L_len:
        sorted_arr.append(L[l])
        l += 1

    while r < R_len:
        sorted_arr.append(R[r])
        r += 1

    return sorted_arr

arr = [12, -1, 2, 14, 67, 34, 64, 63, -11]
print(merge_sort(arr))