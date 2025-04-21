#this code to find the missing number in the list
arr = [1,4,6,2,7,9,8,5]

def missingNumberInArray(arr):
    summ  = sum(arr)
    n = len(arr) + 1
    total = n * (n+1) // 2
    return total - summ

print(missingNumberInArray(arr))