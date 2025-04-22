'''
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0

dont have to count the frequency since the jewels are not repitative so hashset or set is usefull here

'''



j = "aaB"
s = "aaBBii"
def numJewelsInStones(jewels, stones) -> int:
    
    count = 0

    for chars in stones:
        if chars in set(jewels):
            count += 1
        else:
            continue
    return count

print(numJewelsInStones(j,s))