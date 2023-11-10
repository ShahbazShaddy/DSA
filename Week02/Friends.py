#------------------------------  (a)  ------------------------------#
def friendSlower(A):
    pairs = []

    n = len(A)
    for i in range(n): #O(n^2)
        for j in range(i+1, n): 
            if A[i][1] >= A[j][0] and A[i][0] <= A[j][1]:
                pairs.append((i+1, j+1)) # +1 because of 1-based indexing

    return pairs

A = [[1, 4], [2, 5], [7, 9], [9, 10], [6, 10]]
result = friendSlower(A)
print(result)

#------------------------------  (b)  ------------------------------#

# In Friends.py

# In Friends.py

# In Friends.py

def friendsFaster(A):
    events = []
    for i in range(len(A)):
        events.append((A[i][0], 'enter', i))
        events.append((A[i][1], 'exit', i))

    events.sort()

    count = 0
    pairs = set()

    for event in events:
        if event[1] == 'enter':
            count += 1
        else:
            for other_event in events:
                if other_event[1] == 'enter' and other_event[2] != event[2]:
                    pairs.add((min(other_event[2] + 1, event[2] + 1), max(other_event[2] + 1, event[2] + 1)))

    return list(pairs)



A = [[1, 4], [2, 5], [7, 9], [9, 10], [6, 10]]
result = friendsFaster(A)
print(result)
