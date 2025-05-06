'''
Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

'''
nums = [2,3,1,2,4,3]
target = 7

def minSubArrayLen(nums, target):
    n = len(nums)                               
    left = 0
    current_sum = 0                                                     # To storethe current window sum (will increase in the for loop until we get a value >= target)
    min_lenght = float('inf')

    for right in range(n):
        current_sum += nums[right]

        while current_sum >= target:                                    # If we get a value that is greater tha nr equal to target we will measure the lenght
            min_lenght = min(min_lenght, right - left + 1)              # And we will decrease the size from the size from left because we need minimal lenght
            current_sum -= nums[left]
            left += 1                                                   # And while decreasing the length we we find that the current sum is not satisfying our condition we will exit and return to the for loop and increase the size by nums[right]

    return min_lenght


print(minSubArrayLen(nums,target))