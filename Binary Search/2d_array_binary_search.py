# Not best case
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9,34],
    [1]
]
target = 12

def bianry_search(arr,target):
    for i in range(len(arr)):
        left, right = 0, len(arr[i]) -1

        while left <= right:
            mid = left + (right - left) //2
            if arr[i][mid] == target:
                return True
            elif arr[i][mid] < target:
                left += 1
            else:
                right -= 1
    return False

print(bianry_search(arr,target))