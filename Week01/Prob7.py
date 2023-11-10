# Import necessary functions from funcs.py
import funcs, Bubble, Selection, Insertion, HybridMerge
import time
import csv

# Read values of n from Nvalues.txt
with open("Nvalues.txt", "r") as file:
    n_values = [int(line.strip()) for line in file]

# Create a list of sorting functions
sorting_functions = [
    ("Bubble Sort", Bubble),
    ("Selection Sort", Selection),
    ("Insertion Sort", Insertion),
    ("Hybrid Merge Sort", HybridMerge),
]

# Open the CSV file for writing
with open("RunTime.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write the header row
    csvwriter.writerow(["n", "Sorting Algorithm", "Time Taken (seconds)"])

    # Iterate through each value of n
    for n in n_values:
        array = funcs.generateRandomArray()  # Generate a random array of size n

        # Iterate through each sorting function
        for algorithm_name, sorting_function in sorting_functions:
            array_copy = array.copy()  # Create a copy of the original array

            start_time = time.time()
            sorting_function(
                array_copy, 0, len(array_copy) - 1, n
            )  # Assuming HybridMergeSort also follows the (array, start, end, n) prototype
            end_time = time.time()

            time_taken = end_time - start_time
            csvwriter.writerow([n, algorithm_name, time_taken])
