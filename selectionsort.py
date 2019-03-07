#!/usr/bin/env python3


def selection_sort(arr):
    for i in range(len(arr)):

        # set left to the original incrementor
        # and set right to the index after
        left = i
        right = i + 1

        # walk through array with right
        # and put smallest in left (aka select it).
        # This ensures that left is the smallest
        # value on the right hand side of array
        while right < len(arr):
            if arr[right] < arr[left]:
                left = right
            right += 1

        # if left was swapped, put it in the array
        # by swapping it with element at current index
        if left != i:
            tmp = arr[i]
            arr[i] = arr[left]
            arr[left] = tmp


my_arr = [11, 42, 20, 8, 9, 2, 5, 3]

print(my_arr)
selection_sort(my_arr)
print(my_arr)
