'''
977. Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

'''
nums = [-4,-1,0,3,10]

def sortedSquares(nums):
    result = []                                             # Result array to store the output after sorting
    left, right = 0, len(nums) -1

    for n in range(len(nums)):                              # For storing the square of the elements we can skip this also
        square  = nums[n] * nums[n]
        nums[n] = square
    
    while left <= right:                                    # two pointer for comparing 
        if nums[left] > nums[right]:
            result.append(nums[left])
            left += 1
        else:
            result.append(nums[right])
            right -=1

    result.reverse()                                        # Untill this it stores the elements in decreasing order so we need to reverse it 
    return result

print(sortedSquares(nums))


# Another solution - 

nums = [-4,-1,0,3,10]

def sortedSquares(nums):
    n = len(nums)                                                       # Lenght of the original array
    result = [0] * n                                                    # Result array (by deault it is set ot 0 with the length of nums)
    left, right = 0, n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):                           # Since a higher value will oviously produce higher square so we compare that here
            result[n - 1] = nums[left] ** 2                              # after finding the value we store the square root in the end of the result array
            left += 1
            
        else:
            result[n - 1] = nums[right] ** 2
            right -= 1
        n -= 1                                                           # decreases the size by the size of nums by 4, 3, 2,1, 0
        print(n)                                                         # for printing it out                                                          

    return result

print(sortedSquares(nums))