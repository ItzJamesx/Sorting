#!/usr/bin/env python3


def merge_sort(arr):
    # stop at last element
    if len(arr) > 1:

        # set the bounds on our array
        # split left and right into sub-arrays
        mid = int(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]

        # recursively call on the sub-arrays
        # until they are 1 element
        merge_sort(left)
        merge_sort(right)

        # right index
        ri = 0
        # left index
        li = 0
        # input/output array index
        ai = 0

        # walk through left and right sub-arr
        # adding the smallest to the array
        while li < len(left) and ri < len(right):
            if left[li] < right[ri]:
                arr[ai] = left[li]
                li = li + 1
            else:
                arr[ai] = right[ri]
                ri = ri + 1

            ai += 1

        # append remaining elements
        # on the main array so they are not
        # lost/overwritten in subsequent calls
        while li < len(left):
            arr[ai] = left[li]
            li = li + 1
            ai = ai + 1

        while ri < len(right):
            arr[ai] = right[ri]
            ri = ri + 1
            ai = ai + 1


my_arr = [4, 6, 3, 9, 0, 2, 7]

print(my_arr)
merge_sort(my_arr)
print(my_arr)
