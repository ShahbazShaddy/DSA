import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('dailySteps_merged.csv' )
Days = df['ActivityDay'].values.tolist()
Steps = df['StepTotal'].values.tolist()
plt.plot(Days,Steps)
plt.show()

df = pd.read_csv('dailyActivity_merged.csv' )
Date = df['ActivityDate'].values.tolist()
Distance = df['TotalDistance'].values.tolist()
plt.bar(Date,Distance)
plt.show()

df = pd.read_csv('sleepDay_merged.csv' )
Date = df['SleepDay'].values.tolist()
Time = df['TotalTimeInBed'].values.tolist()
plt.scatter(Date,Time)
plt.show()

ArraySteps = []
df = pd.read_csv('hourlySteps_merged.csv' )
Steps = df['StepTotal'].values.tolist()
for i in range(24):
  ArraySteps.append(Steps[i])
plt.pie(ArraySteps)
plt.show()