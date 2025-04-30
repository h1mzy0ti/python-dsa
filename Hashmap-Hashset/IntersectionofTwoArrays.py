'''

Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 
'''
nums1 = [1,2,2,1]
w = [2,2]

def intersection(nums1, nums2):
        res = []
        n1set,n2set = set(nums1),set(nums2)                             # Redues duplicated and Time complexity (VERY IMPORTANT)

        for v in n2set:                                                 # Simple and fast
            if v in n1set:
                res.append(v)

        return res

print(intersection(nums1,w))

# Time - O(n + m)
# space - O(n + m)

#This solution is as efficient as it gets unless the arrays are 
#sorted, in which case a two-pointer approach could use slightly less space (O(1) if no set is used).