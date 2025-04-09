# Adding and int array 
def add_arr(arr):
    sum = 0
    for i in range (len(arr)):
        sum = sum + arr[i]
    if sum == 28:
        return True
    else:
        return sum


arr = [1,2,3,4,5,6,7]
print(add_arr(arr))