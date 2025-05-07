'''
You are given an array nums consisting of positive integers.
We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
Return the length of the longest nice subarray.
A subarray is a contiguous part of an array.
Note that subarrays of length 1 are always considered nice.

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.


                            Bitmask Operators in Python
___________________________________________________________________________________________
Operator	     Symbol	        Name	            Description                            |
-------------------------------------------------------------------------------------------|
AND	                &	     Bitwise AND	    1 if both bits are 1                       |
OR	                |	     Bitwise OR	        1 if either bit is 1                       |
XOR	                ^	     Bitwise XOR	    1 if only one bit is 1                     |
NOT             	~	     Bitwise NOT	    Flips all bits (inverts)                   |
SHIFT L	            <<	     Left Shift	        Shifts bits left (multiply by 2 each shift)|
SHIFT R	            >>	     Right Shift	    Shifts bits right (divide by 2 each shift) |
___________________________________________________________________________________________|

'''
nums = [1,3,8,48,10]
 
def longestNiceSubarray(nums):
    n = len(nums)
    left = 0
    bitmask = 0
    max_substring = 0

    for right in range(n):
        while (bitmask & nums[right]) != 0:
            bitmask ^= nums[left]                                                               # remove nums[left] from bitmask
            left += 1
        
        bitmask |= nums[right]
        max_substring = max(max_substring, right - left + 1)
        
    return max_substring 

print(longestNiceSubarray(nums))
