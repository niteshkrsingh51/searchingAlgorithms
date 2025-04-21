#this code to find the largest three numbers in the list
arr = [1,4,2,7,9,5]

def thirdLargestInArray(arr):
    if len(arr) < 2:
        return -1
    largestNum,secondLargest,thirdLargest = 0,0,0
    for i in arr:
        if i > largestNum:
            thirdLargest = secondLargest
            secondLargest = largestNum
            largestNum = i
        elif i > secondLargest and i != largestNum:
            thirdLargest = secondLargest
            secondLargest = i
        elif i > thirdLargest and i != secondLargest and i != largestNum:
            thirdLargest = i
    return thirdLargest

print(thirdLargestInArray(arr))