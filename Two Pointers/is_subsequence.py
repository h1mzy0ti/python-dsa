'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining 
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Input: s = "abc", t = "ahbgdc"
Output: true
'''
s = "abc"
t = "ahbgdc"

def isSubsequence( s: str, t: str) -> bool:
    sl = len(s)                                     # lenght of s 
    p = 0                                           # Pointer to track the len of s

    for char in t:                                  # Looping through elements of the t
        if p < sl and s[p] == char:                 # if element of p == char then p + 1
            p += 1  
                                                    # if not then return to the the loop again to complete the iteration of char in t
    return  p == sl                             # then return if the value of p is == to lenght of s or sl(len)

print(isSubsequence(s,t))



