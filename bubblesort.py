#!/usr/bin/env python3


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp


my_arr = [12, 45, 19, 8, 9, 2, 5, 3]

print(my_arr)
bubble_sort(my_arr)
print(my_arr)
