arr = [23,4,2,12,-12]
def bubbleSort(arr):

    n = len(arr) -1
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubbleSort(arr))