def mySort(arr):
    array = arr
    sorted = []
    index = 0

    while True: 
        for i in array:
            if i == index:
                sorted.append(i)

        index += 1

        if len(sorted) == len(array):
            break

    return sorted

array = [1,5,3,6,7,4,3,1,6,8,10]

print(f'raw-array: {array}')
print(f'sorted-array: {mySort(array)}')