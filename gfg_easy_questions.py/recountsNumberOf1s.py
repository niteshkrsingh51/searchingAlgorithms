# Returns counts of 1's in arr[low..high]. 
# The array is assumed to be sorted in 
# non-increasing order
def count_ones(arr):
    n = len(arr)
    low,high = 0,n-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == 0:
            high = mid - 1
        elif arr[mid] == n - 1 or arr[mid+1] != 1:
            return mid+1
        else:
            low = mid + 1
    return 0

arr = [1, 1, 1, 1, 0, 0, 0]
print(count_ones(arr))