'''
441. Arranging Coins

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
________
| C |   |
| C | C |
| C | C |
---------
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

________
| C |   |
| C | C |___
| C | C | C |
| C | C |   |
------------
Input: n = 8
Output: 3

'''
# every coins should be like this - 
# if n is 8 - it will be 1 to 8 and 1 will have 1 stair block and 2 will have 2 block and 3 will have 3 blocks
# we will know the stair is completed when we get the same as the previous one or smaller than the previous one 
n = 5
def arrangeCoins(n) :
    left,right = 0, n

    while left <= right:
        


2 * 2 / 2













print(arrangeCoins(n))