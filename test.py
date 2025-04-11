nums = [23,2,14,12]
def isMonotonic(nums):

    for n in range(len(nums)-1):
        if nums[n] > nums[n+1]:
            return False
        elif nums[n] < nums[n+1]:
            return False
    return True
print(isMonotonic(nums))