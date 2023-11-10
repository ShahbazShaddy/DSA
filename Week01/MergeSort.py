import random
import time
import csv
import funcs

def MergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2

        MergeSort(arr, start, mid)
        MergeSort(arr, mid + 1, end)
        Merge(arr, start, mid, end)

def Merge(arr, p, q, r):
    left = arr[p:q+1]
    right = arr[q+1:r+1]

    i = j = 0
    k = p

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

# Generate a random array of integers
randomArray = funcs.generateRandomArray()

# Measure the time taken for sorting using Merge Sort
startTime = time.time()
MergeSort(randomArray, 0, len(randomArray)-1)
endTime = time.time()
timeTaken = endTime - startTime
print("Sorting took", timeTaken, "seconds.")

# Write the sorted array to a CSV file
with open('SortedMergeSort.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for num in randomArray:
        csvwriter.writerow([num])