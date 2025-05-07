'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.


Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

'''
s = "abcabcbb"
def lengthOfLongestSubstring(s):
    n = len(s)
    res = set()                                                     # set to not store duplicate
    right = 0                                                       # to  increase the size 
    left = 0                                                        # to decrease the size 
    max_sub = 0                                                     # to count the size 

    for right in range(n):                                          # looping through the size of s
        while s[right] in res:                                      # if found duplicate then
            res.remove(s[left])                                    # shrink the size by left
            left += 1

        res.add(s[right])                                           # adding the elements
        max_sub = max(max_sub,right - left + 1)                     # and counting the length
            

    return max_sub  
            


print(lengthOfLongestSubstring(s))