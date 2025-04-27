'''
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Almost simialr to next greater element

'''

temperatures = [73,74,75,71,69,72,76,73]


def dailyTemparatures(t):
    stack = []                                              # Stack to store the indexs
    result = [0] * len(t)                                   # Main list to store the output by default it is 0

    for nums in range(len(t)):
        while stack and t[nums] > t[stack[-1]]:             # Condition if the current t[nums] i greater than the t[stack] where stack is 
            index = stack.pop()                             # storing the index
            result[index] = nums - index                    # if greater than append to result - in the index of result append nums(index only) - index of the top stack 
        stack.append(nums)                                  # if stack is empty and t[nums](also cuurent element) is not greater than the top of the stack(index) 
    return result


print(dailyTemparatures(temperatures))