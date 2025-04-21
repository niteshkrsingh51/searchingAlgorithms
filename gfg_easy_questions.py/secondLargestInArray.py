#this code to find the second largest number in the list
arr = [1,4,2,7,9,5]

def secondLargestInArray(arr):
    if len(arr) < 2:
        return -1
    largestNum,secondLargest = 0,0
    for i in arr:
        if i > largestNum:
            secondLargest = largestNum
            largestNum = i
        elif i > secondLargest and i != largestNum:
            secondLargest = i
    return secondLargest

print(secondLargestInArray(arr))