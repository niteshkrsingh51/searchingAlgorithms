import sys
#this code to find the closest to zero in the list
arr = [2,1,4,6,-9]

def closestTwoCurrSumZero(arr):
    arr1 = sorted(arr)
    low,high = 0,len(arr1)-1
    mincurr_sum = sys.maxsize
    x1,x2 = None,None
    while low < high:
        curr_sum = arr1[low] + arr1[high]
        if abs(curr_sum) < abs(mincurr_sum):
            mincurr_sum = curr_sum
            x1,x2 = low,high
        if curr_sum < 0:
            low += 1
        else:
            high -= 1
    return (abs(arr1[x1] + arr1[x2])) if x1 is not None and x2 is not None else None

print(closestTwoCurrSumZero(arr))