#!/usr/bin/env python


def merge_sort(arr):

    if len(arr) > 1:

        mid = int(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        # right index
        ri = 0
        # left index
        li = 0
        # output array index
        ai = 0

        while li < len(left) and ri < len(right):
            if left[li] < right[ri]:
                arr[ai] = left[li]
                li = li + 1
            else:
                arr[ai] = right[ri]
                ri = ri + 1
            ai = ai + 1

        while li < len(left):
            arr[ai] = left[li]
            li = li + 1
            ai = ai + 1

        while ri < len(right):
            arr[ai] = right[ri]
            ri = ri + 1
            ai = ai + 1


my_arr = [1, 4, 8, 9, 2, 5, 3, 8, 7]

print(my_arr)
merge_sort(my_arr)
print(my_arr)
