def two_pointer(arr,target):

    arr.sort()
    left, right = 0, len(arr) - 1

    while left<right:
        sum = arr[left] + arr[right]

        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -=1

    return False

arr = [1,3,4,56,7,55,44,89]
target = 111
print(two_pointer(arr,target))