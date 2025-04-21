word1 = "abc"
word2 = "pqrt"
# Expected oputput = apbqcr

def mergeAlternately(word1: str, word2: str) -> str:
    w1l,w2l = len(word1), len(word2)                # for lenght
    res = []                                        # To store the each letter after one iteration

    for i in range(max(w1l,w2l)):                   # Contdition to  run untill the max lenght
        if i < w1l:                                 # if i is less than the lenght of word1 the letter will be added otherwise pass
            res.append(word1[i])
        if i < w2l:                                 # if i is less than the lenght of word2 the letter will be added otherwise pass
            res.append(word2[i])

    return ''.join(res)                             # Trick to convert the list into string where ''.join(res)

print(mergeAlternately(word1,word2))

# Time = O(n)
# Space = O(n)