from collections import deque
dq = deque()

arr = [1, 2, 3, 4, 5]


dq.append(arr[0])
dq.append(arr[1])
dq.append(arr[2])

dq.appendleft(arr[3])
dq.appendleft(arr[4])

dq.pop()
dq.popleft()

print(dq)
