# Implementation of Graph

import random
import matplotlib.pyplot as plt
import pandas as pd

class Student:
    def __init__(self, RollNum, Name, Marks):
        self.RollNum = RollNum
        self.Name = Name
        self.Marks = Marks

students = [Student(i, f'Student{i}', random.uniform(1, 100)) for i in range(500)]

# Plotting RollNum vs Marks
plt.figure(figsize=(10, 6))
plt.plot([student.RollNum for student in students], [student.Marks for student in students])
plt.xlabel('RollNum')
plt.ylabel('Marks')
plt.show()

def bubbleSort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j].Marks > arr[j+1].Marks:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count

# Performance graph
n_values = list(range(10, 1001, 10))
swap_counts = [bubbleSort(students[:n]) for n in n_values]

plt.figure(figsize=(10, 6))
plt.plot(n_values, swap_counts)
plt.xlabel('n')
plt.ylabel('Number of swaps')
plt.show()

# Store in CSV
df = pd.DataFrame({'n': n_values, 'swaps': swap_counts})
df.to_csv('performance.csv', index=False)