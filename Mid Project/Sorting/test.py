def bubbleSort(arr):
    n = len(arr)
    indexed_arr = [(arr[i], i) for i in range(n)]
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater
            # than the next element
            if indexed_arr[j][0] > indexed_arr[j + 1][0]:
                indexed_arr[j], indexed_arr[j + 1] = indexed_arr[j + 1], indexed_arr[j]
                swapped = True
            if not swapped:
                return
    # Extract sorted elements and corresponding indices
    sorted_elements = [item[0] for item in indexed_arr]
    original_indices = [item[1] for item in indexed_arr]

    return sorted_elements, original_indices
