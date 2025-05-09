nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

def longestOnes(nums,k):
    n = len(nums)
    left = 0
    maximum = 0
    zero_count = 0

    for right in range(n):

        if nums[right] == 0:
            zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

        maximum = max(maximum,right - left + 1)
    return maximum

print(longestOnes(nums,k))