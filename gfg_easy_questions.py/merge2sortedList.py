arr1 = [1,3,4,8]
arr2 = [2,5,6,7,9]

def mergeSortedList(arr1,arr2):
    if arr1 != sorted(arr1) or arr2 != sorted(arr2):
        raise ValueError("Both input arrays must be sorted.")
    i=0
    j=0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    return merged + arr1[i:] + arr2[j:]

print(mergeSortedList(arr1,arr2))
# Time Complexity: O(n+m) where n is the length of arr1 and m is the length of arr2