#implement quick sort in just even indexes

def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    for i in range(start, end, 2):  # Step through the array by 2
        if arr[i] <= pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 2  # Increase pIndex by 2
    arr[pIndex], arr[end] = arr[end], arr[pIndex]
    return pIndex

def quickSort(arr, start, end):
    if start < end:
        pIndex = partition(arr, start, end)
        # Ensure that the recursive calls for quickSort only consider even indexes
        if pIndex-2 > start:
            quickSort(arr, start, pIndex-2)
        if pIndex+2 < end:
            quickSort(arr, pIndex+2, end)
arr = [9, 8, 7, 6, 5, 4, 3, 2, 10, 1,3,2, 1]
quickSort(arr, 0, len(arr)-1)
print(arr)
