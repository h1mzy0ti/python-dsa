def threesum(nums,target):
    nums.sort()
    rs = []
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l,r = i + 1, len(nums) -1
        while l < r:
            threesum =  a + nums[l] + nums[r]
            if threesum == target:
                return threesum
            elif threesum < target:
                rs.append(threesum)
                l += 1
            else:
                rs.append(threesum)
                r -= 1


    return min(rs, key=lambda x: abs(x - target))

nums = [1,1,1,1]
target = 1
print(threesum(nums,target))