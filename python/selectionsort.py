#!/usr/bin/env python


def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[min]:
                min = j
            j = j+1

        if min != i:
            tmp = arr[i]
            arr[i] = arr[min]
            arr[min] = tmp


my_arr = [1, 4, 8, 9, 2, 5, 3]

print(my_arr)
selection_sort(my_arr)
print(my_arr)
