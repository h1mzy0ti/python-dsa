'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.


Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

'''
s = "ABAB"
k = 2

def characterReplacement(s, k):
    n = len(s)
    count = [0] * 26  # For 'A' to 'Z'
    left = 0
    max_freq = 0
    max_len = 0

    for right in range(n):
        index = ord(s[right]) - ord('A')
        count[index] += 1

        max_freq = max(max_freq, count[index])

        while (right - left + 1) - max_freq > k:
            count[ord(s[left]) - ord('A')] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


print(characterReplacement(s,k))