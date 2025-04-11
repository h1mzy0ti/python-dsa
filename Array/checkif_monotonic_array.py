arr = [3,2,1]

def check_monotonic(arr):
    i = True
    d = True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            i = False
        if arr[i] < arr[i + 1]:
            d = False
    
    return i or d

print(check_monotonic(arr))
