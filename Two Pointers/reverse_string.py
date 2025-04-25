'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

'''

s = ["h","e","l","l","o"]

def reverseString(s):
    l,r = 0, len(s) -1
    
    while l < r:
        s[l], s[r] = s[r], s[l]                     # In place direct swapping (if done line by line or 
        l += 1                                      # l to r first and r to l than it wont swap correctly)
        r -= 1
        
    return s


print(reverseString(s))

