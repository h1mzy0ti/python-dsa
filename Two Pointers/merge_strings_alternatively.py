word1 = "abc"
word2 = "pqrt"
# Expected oputput = apbqcr
def mergeAlternately(word1: str, word2: str) -> str:
    w1l,w2l = len(word1), len(word2)
    res = []

    for i in range(max(w1l,w2l)):
        if i < w1l:
            res.append(word1[i])
        if i < w2l:
            res.append(word2[i])

    return ''.join(res)

print(mergeAlternately(word1,word2))

# Time = O(n)
# Space = O(n)