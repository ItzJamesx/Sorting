#!/usr/bin/env python3


def quick_sort(arr, low, high):

    if low < high: 
        # si can mean small index or start index
        si = (low - 1)

        # arbitrarily pick the last value
        pivot = arr[high]

        # this loop makes all values that
        # are less than the pivot value swap places
        # with the small index
        for ai in range(low, high):
            # ai is array index
            if arr[ai] <= pivot:
                si += 1
                arr[si], arr[ai] = arr[ai], arr[si]

        # swap pivot and start index
        arr[si+1], arr[high] = arr[high], arr[si+1]

        # like merge sort, we recursively
        # call with new bounds
        quick_sort(arr, low, si) 
        quick_sort(arr, si+1, high) 


my_arr = [4, 9, 2, 5, 3, 9, 8, 10, 40, 90, 20]
hi = len(my_arr) - 1

print(my_arr)
quick_sort(my_arr, 0, hi)
print(my_arr)

