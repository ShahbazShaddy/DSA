import time
import csv
import funcs

def insertionSort(arr, start, end):
    for i in range(start + 1, end + 1):
        temp = arr[i]
        j = i - 1
        while j >= start and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr

# Generate a random array of integers
randomArray = funcs.generateRandomArray()

# Measure the time taken for sorting using Insertion Sort
startTime = time.time()
insertionSort(randomArray, 0, len(randomArray) - 1)
endTime = time.time()
timeTaken = endTime - startTime
print("Sorting took", timeTaken, "seconds.")

# Write the sorted array to a CSV file
with open('SortedInsertionSort.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for num in randomArray:
        csvwriter.writerow([num])
