#!/usr/bin/env python3


def insertion_sort(arr):
    for i in range(len(arr)):

        # j will be the element that gets "inserted" in the list.
        # We can assume that the left side of the array is sorted
        # from the following loop
        j = i

        # every new element we reach in the array, we
        # 1.) check if the index (j) is less than the one before AND less than the previous element
        # 2.) if so, swap the two values and
        # 3.) decrement the list
        while j > 0 and arr[j] < arr[j - 1]:
            tmp = arr[j - 1]
            arr[j - 1] = arr[j]
            arr[j] = tmp
            j = j - 1


my_arr = [4, 8, 3, 1, 9, 7]


print(my_arr)
insertion_sort(my_arr)
print(my_arr)
