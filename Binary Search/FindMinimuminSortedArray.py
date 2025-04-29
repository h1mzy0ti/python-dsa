'''
Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

'''
nums = [3,4,5,1,2]

def findMin(nums):                                          # here we dont know the target so we do comapre wth the mid
   
    left, right = 0, len(nums) -1                           # Typical Binary search initialization

    while left < right:                                     # Main condition for the loop
        mid = left + (right - left) // 2
                                                            # Here we know that half part of the array is sorted
        if nums[right] >= nums[mid]:                        # If right is greater than the mid than we know it is on the other side (left)
            right = mid                                     # Here we know the right is less than mid, so we pass it to the next for left
            
        elif nums[left] <= nums[mid]:                       # If left is smaller than the mid we know  it is in the other side of the mid since the right passed it
            left = mid + 1                                  # Than we pass left to be the mid+1 since the mid is already checked

    return nums[left]

print(findMin(nums))

