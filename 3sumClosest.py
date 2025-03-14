def threeSumClosest(nums,target):
    nums.sort()
    res = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l,r = i + 1, len(nums) - 1

        while l < r:
            threesum = a + nums[l] + nums[r]

            if threesum == target:
                return threesum
            elif threesum < target:
                res.append(threesum)
                l += 1
            else:
                res.append(threesum)
                r -= 1
    return min(res, key=lambda x: abs(x - target))

nums = [-1,2,1,-4]
target = 1
print(threeSumClosest(nums,target))