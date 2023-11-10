import random
import time
import csv
import funcs

def bubbleSort(arr, start, end):
    for i in range(start, end):
        for j in range(start, end-i):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp


# Generate a random array
randomArray = funcs.generateRandomArray()

# Measure the time taken for sorting using Bubble Sort
startTime=time.time()
bubbleSort(randomArray,0,len(randomArray)-1)
endTime=time.time()
timeTaken=endTime-startTime
print("Sorting took",timeTaken,"seconds.")

# Write the sorted array to a CSV file
with open('SortedBubbleSort.csv','w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile)
    for i in randomArray:
        csvwriter.writerow([i])