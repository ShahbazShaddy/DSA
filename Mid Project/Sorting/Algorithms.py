import time


def insertionSort(arr, indices):
    for i in range(1, len(arr)):
        key = arr[i]
        index_key = indices[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            indices[j + 1] = indices[j]
            j -= 1
        arr[j + 1] = key
        indices[j + 1] = index_key
    return arr, indices


def bucketSort(x, ui):
    max_val = max(x)
    min_val = min(x)
    bucket_range = (max_val - min_val) / 10

    buckets = [[] for _ in range(10)]

    # Put array elements into buckets
    for num in x:
        bucket_index = int((num - min_val) // bucket_range)
        if bucket_index != 10:  # Ensure the last bucket is not out of range
            buckets[bucket_index].append(num)

    # Sort individual buckets and update indices
    sorted_elements = []
    indices = []
    total_elements = sum([len(bucket) for bucket in buckets])
    processed_elements = 0
    for i in range(10):
        if buckets[i]:
            sorted_bucket, bucket_indices = insertionSort(buckets[i],
                                                          [index for index in range(len(x)) if x[index] in buckets[i]])
            sorted_elements.extend(sorted_bucket)
            indices.extend(bucket_indices)
            processed_elements += len(sorted_bucket)
            progress_percentage = (processed_elements / total_elements) * 100
            ui.progressBar.setValue(progress_percentage)
            ui.progressBar_admin.setValue(progress_percentage)
            time.sleep(0.1)

    return sorted_elements, indices


def mergeSort(arr, ui):
    if len(arr) <= 1:
        return arr, list(range(len(arr)))

    # Finding the mid of the array
    mid = len(arr) // 2

    # Dividing the array elements into 2 halves
    L, L_indices = mergeSort(arr[:mid], ui)
    R, R_indices = mergeSort(arr[mid:], ui)
    i = j = k = 0
    sorted_arr = [0] * len(arr)
    sorted_indices = [0] * len(arr)

    # Merge the sorted halves and track the indexes
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            sorted_arr[k] = L[i]
            sorted_indices[k] = L_indices[i]
            i += 1
        else:
            sorted_arr[k] = R[j]
            sorted_indices[k] = R_indices[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        sorted_arr[k] = L[i]
        sorted_indices[k] = L_indices[i]
        i += 1
        k += 1

    while j < len(R):
        sorted_arr[k] = R[j]
        sorted_indices[k] = R_indices[j]
        j += 1
        k += 1

    return sorted_arr, sorted_indices


def bubbleSort(arr,ui):
    global progress
    n = len(arr)
    count = 0
    # Create a list of tuples (element, original_index)
    indexed_arr = [(arr[i], i) for i in range(n)]
    swap = True
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater
            # than the next element
            if indexed_arr[j][0] > indexed_arr[j + 1][0]:
                indexed_arr[j], indexed_arr[j + 1] = indexed_arr[j + 1], indexed_arr[j]
                swap = True
                count += 1
            progress = (i * (n - i - 1)) / 2 + j
            progress_percentage = (count / n) * 100
            ui.progressBar.setValue(progress_percentage)
            ui.progressBar_admin.setValue(progress_percentage)
            # time.sleep(0.1)
            if not swap:
                return
    sorted_elements = [item[0] for item in indexed_arr]
    original_indices = [item[1] for item in indexed_arr]

    return sorted_elements, original_indices
