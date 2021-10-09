"""
Program of shell sort
"""

def shellSort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
    # Sort the sub input_arr for this gap
    while j >= gap and arr[j - gap] > temp:
        arr[j] = arr[j - gap]
        j = j-gap
        arr[j] = temp
    # Reduce the gap for the next element
    gap = gap//2

if __name__ == "__main__":
    input_arr = [19,2,31,45,30,11,121,27]
    shellSort(input_arr)
    print(input_arr)