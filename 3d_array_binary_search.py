# Not best case
arr = [[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9,34],
    [1]],[[1,2,3],[1,5,7]]
]
target = 1

def binary_search(arr,target):
    for i in range (len(arr)):
        left, right = 0, len(arr[i][i]) -1
        while left <= right:
            mid  = left + (right - left) //2
            if arr[i][i][mid] == target:
                return True
            elif arr[i][i][mid] < target:
                left += 1
            else:
                right -= 1
    return False
print(binary_search(arr,target))
