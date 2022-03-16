def max_sequence(arr):
    arrayOfSums = []
    for i in range(len(arr)):
        if i < len(arr) - 1:
            arrayOfSums.append(arr[i] + arr[i+1] + arr[i+2] + arr[i+3])

    return max(arrayOfSums)
