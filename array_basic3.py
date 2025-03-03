def min_max(arr):
    int_arr = list(map(int,arr))
    return min(int_arr), max(int_arr)


arr = ["1","2","3","4","5","6","7"]
print(min_max(arr))