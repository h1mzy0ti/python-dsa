# Removing Duplicate
def removing_dup(arr):
    final = set()

    for i in arr:
        if i not in final:
            final.add(i)

    return list(set(arr))

arr = [1,2,3,4,1,4,4,4,4,4,4,4]
print(removing_dup(arr)) 