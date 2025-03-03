# Removing Duplicate
def removing_dup(arr):
    final = set()

    for i in range(len(arr)):
        if arr[i] not in final:
            final.add(i)
        if 0 in final:
            final.remove(0)

    fi = list(final)

    return fi

arr = [1,2,3,4,1,4]
print(removing_dup(arr))