arr = [1,2,,3,4]
target = 5
def two_pointer(arr,target):
    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [left,right]
        elif sum > target:
            right -= 1
        else:
            left += 1
    return False

print(two_pointer(arr,target))

# ONly use two pointer when the array is sorted