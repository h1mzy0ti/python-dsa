'''
Minimum Common Value

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

'''

nums1 = [1,2,3]
nums2 = [2,4]
def getCommon(nums1, nums2):
    n1l, n2l = len(nums1), len(nums2)
    num1P, num2P = 0, 0
    

    while num1P < n1l and num2P < n2l:
        if nums1[num1P] == nums2[num2P]:
            return nums1[num1P]
        
        elif nums1[num1P] < nums2[num2P]:
            num1P += 1
        else:
            num2P += 1
    return -1


print(getCommon(nums1,nums2))