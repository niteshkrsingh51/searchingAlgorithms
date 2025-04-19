def jumpSearch(arry,number):
    jump = round(len(arry)**0.5)
    current = 0
    while arry[current] < number:
        if current + jump >= len(arry)-1:
            current = len(arry)-1
        else:
            current = current + jump

    for i in range(current,current-jump,-1):
        if arry[i] == number:
            return i
    return "Not Found"

arry = [1,2,3,4,5,6,7,8,9,10]
number = 2
print(jumpSearch(arry,number))