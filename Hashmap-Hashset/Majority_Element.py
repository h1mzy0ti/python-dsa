'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

'''

nums = [5,5,5,5,5,53,3,32,2]

def majorityElement(nums):
        elements_frequency = {}                                                 #To store the frequency

        for v in nums:
            if v in elements_frequency:
                elements_frequency[v] += 1
            else:
                elements_frequency[v] = 1
                                                                            
        majority = 0
        majoritykeys = 0
        for k, v in elements_frequency.items():                                 # To count the maximum value from the dictionary
            if v > majority:                                                    # If value of the key is greater than majority(initially = 0)
                majority = v                                                    # update the majority to the current gretest
                majoritykeys = k                                                # Also update the key that contain the highest frequency
        return majoritykeys 

print(majorityElement(nums))