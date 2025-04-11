arr = [2, 1, 3]
stack = []

result = []

for nums in arr:
    while stack and stack[-1] < nums:
        stack.pop()
    result.append(nums)

print(result)
