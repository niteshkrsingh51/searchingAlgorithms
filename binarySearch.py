def binarySearch(arry,number):
    low = 0
    end = len(arry)-1
    while low <= end:
        mid = low + (end - low) // 2
        if arry[mid] == number:
            return mid
        elif number < arry[mid]:
            end = mid - 1
        else:
            low = mid + 1
    return None

def binarySearchWithRecursion(arry,number,high,low):
    if low > high:
        return -1
    mid = low + (high-low)//2
    if arry[mid] == number:
        return mid
    elif arry[mid] < number:
        return binarySearchWithRecursion(arry,number,high,mid+1)
    else:
        return binarySearchWithRecursion(arry,number,mid-1,low)

arry = [2,3,4,5,6,7,8,12]

print(binarySearch(arry,12))

index = binarySearchWithRecursion(arry,12,len(arry)-1,0)
print(index)