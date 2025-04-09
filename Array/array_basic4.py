# Checking elemets if they exists
def element_exist(arr,element):
    int_arr = list(map(int, arr)) 
    if element in int_arr:
        return True
arr = ["1", "2", "3", "4", "5", "6", "7"]
element = 12
print(element_exist(arr,element))