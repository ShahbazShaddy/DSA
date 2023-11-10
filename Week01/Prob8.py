import random
import time
import csv

myfile = open(
    "C:\\Users\\T L S\\Desktop\\Workspace\\3rd Semester\\DSA\\Practice\\2022-CS-27\\words.txt",
    "r",
)
lines = myfile.read()
arr = lines.split("\n")


# MergeSort
# def MergeSort(arr, start, end):
#     if start < end:
#         mid = (start + end) // 2

#         MergeSort(arr, start, mid)
#         MergeSort(arr, mid + 1, end)
#         Merge(arr, start, mid, end)


# def Merge(arr, p, q, r):
#     left = arr[p:q+1]
#     right = arr[q+1:r+1]

#     i = j = 0
#     k = p

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1

#     while i < len(left):
#         arr[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         arr[k] = right[j]
#         j += 1
#         k += 1


# startTime = time.time()
# MergeSort(arr, 0, len(arr) - 1)
# endTime = time.time()
# timeTaken = endTime - startTime
# print("Sorting took by Merge Sort", timeTaken, "seconds.")


# Insertion Sort
def insertionSort(arr, start, end):
    for i in range(start + 1, end + 1):
        temp = arr[i]
        j = i - 1
        while j >= start and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr

startTime = time.time()
insertionSort(arr, 0, len(arr) - 1)
endTime = time.time()
timeTaken = endTime - startTime
print("Sorting took by Insertion Sort", timeTaken, "seconds.")

