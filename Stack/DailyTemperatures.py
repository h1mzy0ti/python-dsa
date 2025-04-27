'''
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

'''
temperatures = [73,74,75,71,69,72,76,73]


def dailyTemparatures(t):
    stack = []
    result = [0] * len(t)

    for nums in range(len(t)):
        while stack and t[nums] > t[stack[-1]]:
            index = stack.pop()
            result[index] = nums - index 
        stack.append(nums)
    return result


print(dailyTemparatures(temperatures))