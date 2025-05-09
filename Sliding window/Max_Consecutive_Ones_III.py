'''
Given a binary array nums and an integer k, return the maximum number of 
consecutive 1's in the array if you can flip at most k 0's.

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

'''
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

def longestOnes(nums,k):
    n = len(nums)
    left = 0
    maximum = 0
    zero_count = 0                                                        # Rather than inseritng into new array by fliping 0 we can count zero

    for right in range(n):

        if nums[right] == 0:                                               # If the right is zero count that and also chec kthe length
            zero_count += 1

            while zero_count > k:                                           # if the zero count is greater than the threshold k
                if nums[left] == 0:                                         # and if count is maxtha nk but also zero is cokking inthe way
                    zero_count -= 1                                         # minus zero if left finds zero
                left += 1                                                   # Increase the left pointer untill its valid will go to the nums[left] == 0


        maximum = max(maximum, right - left + 1)                            # Also check the length

    return maximum









print(longestOnes(nums,k))