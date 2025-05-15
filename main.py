import numpy as np
import time
from sortAlgorithms.quickSort import quickSort
from sortAlgorithms.heapSort import heapSort

def generate_array(n):
    return np.random.randint(1, 1_000_001, size=n, dtype=np.int64)

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        return binarySearch(arr, mid + 1, r, x)
    return -1

def gallopingSearch(arr, n, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    return binarySearch(arr, i // 2, min(i, n - 1), x)

def time_binary_search(arr, x):
    start = time.perf_counter()
    binarySearch(arr, 0, len(arr) - 1, x)
    end = time.perf_counter()
    return (end - start) * 1_000

def time_galloping_search(arr, x):
    start = time.perf_counter()
    gallopingSearch(arr, len(arr), x)
    end = time.perf_counter()
    return (end - start) * 1_000

def time_quickSort(arr):
    start = time.perf_counter()
    # quickSort(arr, 0, len(arr) - 1)
    np.sort(arr, kind="quicksort")
    end = time.perf_counter()
    return (end - start) * 1_000

def time_heapSort(arr):
    start = time.perf_counter()
    # heapSort(arr, len(arr))
    np.sort(arr, kind="heapsort")
    end = time.perf_counter()
    return (end - start) * 1_000

def print_table():
    print(f"{'# de claves':<12} {'Búsqueda Binaria':<25} {'Búsqueda Galopante':<25} {'QuickSort':<25} {'HeapSort':<25}")
    print(f"{'':<12} {'Tiempo (ms)':<25} {'Tiempo (ms)':<25} {'Tiempo (ms)':<25} {'Tiempo (ms)':<25}")
    print("-" * 120)

def main():
    arr = generate_array(500_000_000)
    n = len(arr)
    sizes = [1_000, 5_000, 10_000, 50_000, 100_000]
    arrs = {size: generate_array(size) for size in sizes}
    x = np.random.randint(1, 1_000_001)

    print_table()
    quick_large = time_quickSort(arr)
    heap_large = time_heapSort(arr)
    print(f"{n:<12} {'':<25} {'':<25} {quick_large:<25} {heap_large:<25}")

    for size in sizes:
        arr = arrs[size]
        time_quick = time_quickSort(arr)
        time_heap = time_heapSort(arr)
        time_binary = time_binary_search(arr, x)
        time_galloping = time_galloping_search(arr, x)
        print(f"{size:<12} {time_binary:<25} {time_galloping:<25} {time_quick:<25} {time_heap:<25}")

if __name__ == "__main__":
    main()