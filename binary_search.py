def binary_search(arr,target):
    left, right = 0, len(arr) -1

    while left <= right:
        mid = left + (right - left ) // 2   #OR MID = LEFT + RIGHT // 2 (but not good when the array range is large)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left += 12
        else: right -= 1
    return -1 

arr = [1,2,3,4,5,6,7,8]
target = 6
print("Position is - ",binary_search(arr,target))