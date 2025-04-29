def sortedSquares(nums):
    result = []                                             
    left, right = 0, len(nums) -1

    for n in range(len(nums)):                              
        square  = nums[n] * nums[n]
        nums[n] = square
    
    while left <= right:                                    
        if nums[left] > nums[right]:
            result.append(nums[left])
            left += 1
        else:
            result.append(nums[right])
            right -=1

    result.reverse()                                       
    return result