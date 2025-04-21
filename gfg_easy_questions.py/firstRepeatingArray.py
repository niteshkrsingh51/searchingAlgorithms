#this is a code to find the first repeating element in an array
import sys
arr = [10, 5, 3, 4, 3, 5, 6]

def firstRepeatingNumber(arr):
    seen = set()
    minEle = sys.maxsize
    for i in range(len(arr)-1,-1,-1):
        if arr[i] in seen:
            minEle = min(minEle,i)
        seen.add(arr[i])
    return -1 if minEle == sys.maxsize else arr[minEle]
            
print(firstRepeatingNumber(arr))