'''
1189. Maximum Number of Balloons
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1
Input: text = "loonbalxballpoon"
Output: 2

'''
text = "nlaebolko"

def maxNumberOfBallooons(text):
    freq = {}                                                       # to count the frequency
    for chars in text:
        if chars in freq:
            freq[chars] += 1
        else:
            freq[chars] = 1


    min_balooon = float('inf')                                      # to compare the minumum since the minimum number of the letter is
    b = 'balloon'                                                   # the maximun tiem we can construct balloon
    for char in b:
        if char == "l" or char == "o":
            available = freq.get(char,0) // 2                       # Special case since two 'o' or 'l' in one balloon so floor div for int output
        else:
            available = freq.get(char,0)
        min_balooon = min(min_balooon,available)                    # Compare the minimum each time

    return min_balooon

print(maxNumberOfBallooons(text))


