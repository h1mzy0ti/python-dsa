arr = [1,2,3,3,4,5,5]
hashmap = {}
for nums in arr:
    hashmap[nums] = hashmap.get(nums,0) + 1

print(hashmap)
