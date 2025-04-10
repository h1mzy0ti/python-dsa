from collections import deque
dq = deque()

arr = [12,3,4,56,7,8]

def increasing(arr):
    for nums in arr:
        while dq and dq[-1] < nums:
            dq.pop()
        dq.append(nums)
        print(dq)

def decreasing(arr):
    for nums in arr:
        while dq and dq[-1] > nums:
            dq.append()
        dq.pop(nums)
        print(dq)


increasing(arr)
print("__________")
decreasing(arr)