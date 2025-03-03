# Counting the occurances
def check_occ(arr,check_num):
    int_arr = list(map(int,arr))
    count = 1
    for i in range(len(int_arr)):
        if check_num in int_arr:
            count += 1
            return count
        
arr = ["1","2","1","4"]
check_num = 1
print(check_occ(arr,check_num))