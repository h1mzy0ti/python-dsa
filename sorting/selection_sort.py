arr = [12,45,1.-23,45]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        minval = i
        for j in range (i+1,n):
            if arr[j] < arr[minval]:
                minval = j
        arr[i],arr[minval] = arr[minval],arr[i]
    return arr

print(selection_sort(arr))