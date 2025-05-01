'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

'''
x = 8
def mySqrt(x):
    left,right = 0, x
    res = 0                                                     # Since the output might be in flot so we dont have to retur nthe float but the closest

    while left<= right:
        mid = left + (right - left) // 2

        if mid * mid == x:                                      # Simple case if mid is x
            return mid

        elif mid * mid > x:                                     # if mid * mid is greater than x (we knwo it ant be so we decrease the right by mid - 1)
           right =  mid - 1

        else:                                                   # if mid * mid < x (it is poosbile candidate so we store that and if not we + left with mid)
            left = mid + 1
            res = mid
        
    return res                                                  # if nothing works in the above we return res since the last iteration will be the smallest one
    
        

print(mySqrt(x))



