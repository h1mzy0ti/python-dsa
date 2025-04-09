# Adding an str array
def add_arr(arr):
    sum = 0
    arry = list(map(int,arr))
    for i in range (len(arry)):
        sum = sum + arry[i]
    if sum == 28:
        return True
    else:
        return sum


arr = ["1","2","3","4","5","6","7"]
print(add_arr(arr))