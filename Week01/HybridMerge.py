import random
import csv
import time
import funcs

def HybridMergeSort(arr, start, end, n):
    if end - start <= n:
        insertionSort(arr, start, end)
    else:
        mid = (start + end) // 2
        HybridMergeSort(arr, start, mid, n)
        HybridMergeSort(arr, mid + 1, end, n)
        Merge(arr, start, mid, end)

def insertionSort(arr, start, end):
    for i in range(start + 1, end + 1):
        temp = arr[i]
        j = i - 1
        while j >= start and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def Merge(arr, p, q, r):
    left = arr[p : q + 1]
    right = arr[q + 1 : r + 1]

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


# Measure the time taken for sorting using HybridMergeSort
startTime = time.time()
HybridMergeSort(randomArray, 0, len(randomArray) - 1, n=100)
endTime = time.time()
timeTaken = endTime - startTime
print("Sorting took", timeTaken, "seconds.")

# Write the sorted array to a CSV file
with open('SpetedHybridMergeSort.csv','w', newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    for i in randomArray:
        csvwriter.writerow([i])