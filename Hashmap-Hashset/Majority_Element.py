nums = [5,5,5,5,5,53,3,32,2]
def majorityElement(nums):
        elements_frequency = {}

        for v in nums:
            if v in elements_frequency:
                elements_frequency[v] += 1
            else:
                elements_frequency[v] = 1

        majority = 0
        majorityelement = 0
        for k, v in elements_frequency.items():
            if v > majority:
                majority = v
                majorityelement = k
        return majorityelement 

print(majorityElement(nums))