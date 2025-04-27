# Monotonic Stack (Next Greater Element) same array

arr = [2, 1, 3]

stack = []
result = [-1] * len(arr)

for n in range(len(arr)):
    while stack and arr[n] > arr[stack[-1]]:
        index = stack.pop()
        result[index] = arr[n]
    stack.append(n)


print(result)





