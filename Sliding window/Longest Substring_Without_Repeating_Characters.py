'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.


Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

'''
s = "pwwkew"
def lengthOfLongestSubstring(s):
    n = len(s)
    res = set()                                                     # set to not store duplicate
    right = 0                                                       # to  increase the size 
    left = 0                                                        # to decrease the size 
    max_sub = 0                                                     # to count the size 

    for right in range(n):
        while s[right] in res:
            res.discard(s[left])
            left += 1

        res.add(s[right])
        max_sub = max(max_sub,right - left + 1)
            

    return max_sub
            







print(lengthOfLongestSubstring(s))