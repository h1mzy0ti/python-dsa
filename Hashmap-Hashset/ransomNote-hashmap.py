'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Need to handle the frequency so hashmap is usefull here

'''


r = "aa", m = "ab"

def canConstruct(ransomNote,magazine) -> bool:
        
        freq_count_magagize = {}
        

        for char in magazine:
            if char in freq_count_magagize:
                freq_count_magagize[char] += 1
            else:
                freq_count_magagize[char] = 1

        for char in ransomNote:
            if char in freq_count_magagize and freq_count_magagize[char] > 0:
                freq_count_magagize[char] -= 1
            else:
                return False
        return True
                 

print(canConstruct(r,m))