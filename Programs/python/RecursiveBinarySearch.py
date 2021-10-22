def bsearch(arr, low=0, high=len(arr)-1, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bsearch(arr, low, mid - 1, x)
        else:
            return bsearch(arr, mid + 1, high, x)
    else:
        return -1

arr = [ 3, 9, 11, 23, 58, 69, 112, 530 ]
x = 58
result = bsearch(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list")
