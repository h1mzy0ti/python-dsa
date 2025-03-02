def twoSum( nums, target):
        nums.sort()

        left, right = 0, len(nums) -1

        while left < right:
            sum = nums[left] + nums[right]

            if sum == target:
                return True 
            elif sum < target:
                left += 1
            else:
                right -= 1
        return False

nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))