# Counting the occurances
def check_occ(arr,check_num):
    int_arr = list(map(int,arr))
    check_num = int(check_num)
    count = 0
    for i in int_arr:
        if i ==  check_num:
            count += 1
    return count
    
arr = ["1","2","1","4"]
check_num = 1
print(check_occ(arr,check_num))