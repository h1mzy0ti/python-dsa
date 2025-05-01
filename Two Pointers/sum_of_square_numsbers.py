'''
Sum of Square Numbers

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.


Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false

'''
c = 3
def judgeSquareSum(c):
    left, right = 0, int(c ** 0.5)                                                  # Right is equal to the square root of c

    while left <= right:
        sum_square = left * left + right * right                                    # The original statement( a * a + b * b)

        if sum_square == c:                                                         # If the sum matches the int than return true
            return True
        
        elif sum_square < c:                                                        # if the sum is less than c increase the left
            left += 1
        else:                                                                       # and if the sum is greater than c decrease the right
            righ -= 1
    return False
    

  
print(judgeSquareSum(c))