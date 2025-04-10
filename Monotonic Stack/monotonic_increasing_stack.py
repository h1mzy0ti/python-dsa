# This is an increasing stack 
arr = [5,3,2,6,7,3,2]
monotonic_stack = []

print("Step By Step - ")
for nums in arr:
    while monotonic_stack and monotonic_stack[-1] > nums: # Checks if the top is less or not 
        monotonic_stack.pop()
    monotonic_stack.append(nums)
    print(f"Stack : {monotonic_stack}")

print(f"Remaining : {monotonic_stack}")