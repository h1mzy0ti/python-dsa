
c = 5
def judgeSquareSum(c):
    left, right = 0, int(c**0.5)
    
    while left <= right:
        sumss = left * left + right * right

        if sumss == c:
            return True
        elif sumss < c:
            left += 1
        else:
            right -= 1
    return False

print(judgeSquareSum(c))