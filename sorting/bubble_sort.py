arr = [2,3,1,3,4-12]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
print(bubble_sort(arr)) 