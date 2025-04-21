#this is a code to find the largest element in an array
arr = [1,4,2,7,9,5]

def largetInArray(arr):
    largestNum = arr[0]
    for i in arr:
        if largestNum < i:
            largestNum = i
    return largestNum

print(largetInArray(arr))