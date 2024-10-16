from prac import bubblesort, selectionsort, insertionsort, quicksort, merge, mergesort, heapsort

assert bubblesort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert bubblesort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert selectionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert selectionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert insertionsort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertionsort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert quicksort([4, 6, 2, 9, 1], 0, 1) == [4, 6, 2, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 2) == [2, 4, 6, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 3) == [2, 4, 6, 9, 1]
assert quicksort([4, 6, 2, 9, 1], 0, 4) == [1, 2, 4, 6, 9]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 1) == [2, 3, 1, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 2) == [1, 2, 3, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 3) == [1, 2, 3, 5, 3, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 4) == [1, 2, 3, 3, 5, 2, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 5) == [1, 2, 2, 3, 3, 5, 3]
assert quicksort([3, 2, 1, 5, 3, 2, 3], 0, 6) == [1, 2, 2, 3, 3, 3, 5]

assert merge([1,2,3,5],[4,6,7,8]) == [1,2,3,4,5,6,7,8]

assert mergesort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert mergesort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

assert heapsort([1, 4, 2, 10, 5]) == [1, 2, 4, 5, 10]