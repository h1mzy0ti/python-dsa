# Deque stands for Double ended queue or add or remove from both end (Fifo or Filo/Lifo)

from collections import deque
dq = deque()

'''
dq.append(x)        Add to right
dq.appendleft(x)    Add to left
dq.pop()            Remove from right 
dq.popleft()        Remove from left

'''
arr = [12,3,4,65,78,89]

def append_right(arr):
    for nums in arr:
        dq.append(nums)
    return dq

def append_left(arr):
    for nums in arr:
        dq.appendleft(nums)
    return dq
    
def pop_right():
    dq.pop()
    return dq

def pop_left():
    dq.popleft()
    return dq

print(f"Append Right : {append_right(arr)} \nAppend left :{append_left(arr)}")
print(f"Pop Right :{pop_right()}\nPop Left :{pop_left()}",sep="\n")
