arry = [1,5,4,7,8]

def linearSearch(arry,number):
    for i in range(len(arry)):
        if arry[i] == number:
            print(i)

def lineaSeachWithRecursion(arry,number,index=0):
    if index >= len(arry):
        return -1
    if arry[index] == number:
        return index
    return lineaSeachWithRecursion(arry,number,index+1)

linearSearch(arry,5)
index = lineaSeachWithRecursion(arry,5)
print(index)