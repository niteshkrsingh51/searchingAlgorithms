#this is a code to find the first repeating and missing element in an array
'''Input: arr[] = {4, 3, 6, 2, 1, 1}
Output: 1, 5
Explanation: 5 is missing and 1 is repeating.'''

arr = [4,3,6,2,1,1]

def missingRepeatingNumber(arr):
    n = len(arr)
    sum_n = n * (n+1) // 2
    sum_n1 = n * (n+1) * (2*n+1) // 6

    sum_actual,sum_actual2 = 0,0

    for num in arr:
        sum_actual += num
        sum_actual2 += num*num

    diff = sum_n - sum_actual
    diff_sq = sum_n1 - sum_actual2

    sum_mr = diff_sq//diff

    missing = (diff+sum_mr)//2
    repeating = sum_mr - missing

    return repeating,missing

print(missingRepeatingNumber(arr))
