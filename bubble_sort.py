"""
Implementation of Selection sort in Python 3.7
Time complexity: O(n2)
In-place: yes
Stable: yes
"""

A = [12, 4, 5, 3, 14, 11, 36, 89, 2, 0]

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

print(bubble_sort(A))
