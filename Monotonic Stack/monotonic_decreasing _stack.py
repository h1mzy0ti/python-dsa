arr = [45,2,3,5,6,7,2]
monotonic_stack = []

print("Step By Step - ")
for nums in arr:
    while monotonic_stack and monotonic_stack[-1] < nums:
        monotonic_stack.pop()
    monotonic_stack.append(nums)
    print(f"Stack : {monotonic_stack}")

print(f"Remaining - {monotonic_stack}")