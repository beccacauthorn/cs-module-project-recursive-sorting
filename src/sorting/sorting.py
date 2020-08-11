# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    merged_arr = []

    # Your code here
    indexA = 0
    indexB = 0

    while (len(arrB) - 1 >= indexB) and (len(arrA) - 1 >= indexA):
        if arrA[indexA] < arrB[indexB]:
            merged_arr.append(arrA[indexA])
            indexA = indexA + 1
        else:
            merged_arr.append(arrB[indexB])
            indexB = indexB + 1

    if (len(arrB) - 1 == indexB) and (len(arrA) - 1 == indexA):
        return merged_arr
    else:
        if len(arrB) == indexB:
            if len(arrA) - 1 >= indexA:
                # copy the rest of A
                while len(arrA) - 1 >= indexA:
                    merged_arr.append(arrA[indexA])
                    indexA = indexA + 1
        else:
            if len(arrA) == indexA:
                # copy the rest of B
                while len(arrB) - 1 >= indexB:
                    merged_arr.append(arrB[indexB])
                    indexB = indexB + 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    # break down into two
    arrA = arr[:len(arr) // 2]
    arrB = arr[len(arr) // 2:]

    # sort each of them
    arrA = merge_sort(arrA)
    arrB = merge_sort(arrB)

    # merge them (using helper)
    arr = merge(arrA, arrB)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
