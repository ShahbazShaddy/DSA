import random
import time
import csv
import funcs

def SelectionSort(arr, start, end):
    for i in range(start, end):
        minValue = i
        for j in range(i, end + 1):
            if arr[minValue] > arr[j]:
                minValue = j
        temp=arr[i]
        arr[i]=arr[minValue]
        arr[minValue]=temp

# Generate a random array of integers
randomArray = funcs.generateRandomArray()

# Measure the time taken for sorting using Slection Sort
startTime=time.time()
SelectionSort(randomArray,0,len(randomArray)-1)
endTime=time.time()
timeTaken=endTime-startTime
print("Sorting took",timeTaken,"seconds.")

# Write the sorted array to a CSV file
with open('SortedSelectionSort.csv','w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    for i in randomArray:
        csvwriter.writerow([i])
        