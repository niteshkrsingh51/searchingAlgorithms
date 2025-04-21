arr = [8, 2, 4, 5, 3, 7, 1]

def missingNumber(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    sum_of_arr = sum(arr)
    return total - sum_of_arr

print(missingNumber(arr))  # Output: 6
# Time Complexity: O(n)