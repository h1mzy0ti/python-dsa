'''
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k 
and average greater than or equal to threshold.

 

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3

Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All 
other sub-arrays of size 3 have averages less than 4 (the threshold).


'''
arr = [11,13,17,23,29,31,7,5,2,3]

k = 3
threshold = 5

def numOfSubarrays(arr,k,threshold):
    n = len(arr)
    subarr = 0

    window_sum = sum(arr[:k])

    if window_sum >= threshold * k:                                                 # if the threshold matches count it
        subarr += 1
   
  
    for i in range(k,n):
        window_sum = window_sum -  arr[i - k] + arr[i]                              # by default move the window left to right
        if  window_sum >= threshold * k:                                            # if threshold is found count it 
            subarr +=1


    return subarr 


print(numOfSubarrays(arr,k,threshold))