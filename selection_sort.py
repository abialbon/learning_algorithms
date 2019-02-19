"""
Implementation of Selection sort in Python 3.7
Time complexity: O(n2)
In-place: yes
Stable: no
"""

A = [12, 4, 5, 3, 14, 11, 36, 89, 2, 0]

def selection_sort(A, reverse=False):
    n = len(A)
    f = lambda x, y: x < y
    if (reverse):
        f = lambda x, y: x > y
    for i in range(n-1):
        min_i = i
        for j in range(i+1, n):
            if f(A[j],A[min_i]):
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]
    return A

print(selection_sort(A))
print(selection_sort(A, reverse=True))