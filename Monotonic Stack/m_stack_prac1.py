arr = [2, 1, 3]
stack = []
result = [-1] * len(arr)

for nums in range(len(arr)):
    while stack and arr[nums] > arr[stack[-1]]:
        index = stack.pop()
        result[index] = arr[nums]
    stack.append(nums)

print(result)