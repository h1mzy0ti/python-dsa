'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

'''
s = "IV"

def roman_to_int(s) -> int:
    value_map = {
        "I": 1, 
        "V": 5, "X": 10,
        "L": 50, "C": 100,
        "D": 500, "M": 1000
    }
    total = 0
    previous  = 0

    for v in reversed(s):
        current = value_map[v]
        if current < previous:
            total -= current
        else:
            total += current
        previous = current
    return total

print(roman_to_int(s))
