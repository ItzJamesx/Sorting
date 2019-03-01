#!/usr/bin/env python


def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            tmp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = tmp
            j = j - 1


my_arr = [4, 8, 3, 1, 9, 7]


print(my_arr)
insertion_sort(my_arr)
print(my_arr)
