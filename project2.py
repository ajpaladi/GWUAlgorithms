import time
import math

def missing_in_ap(arr):
    n = len(arr) # is the length of the array
    a = arr[0] # the the first index in the array
    d = (arr[-1] - arr[0]) / n # is the distance between elements
    lo, hi = 0, n - 1 # getting the first and last element 
    while lo < hi: # while last element is less than the first 
        mid = (lo + hi) // 2 # find the midpoint index 
        expected = a + mid * d # calculate the expected value at the index
        if arr[mid] == expected: # if the midpoint == expected value, go right 
            lo = mid + 1
        else: # go left 
            hi = mid
    missing = a + lo * d # continue doing so to find the missing number, which is the first index, minus the low (in the array * distance between elements)
    return round(missing)

def make_ap_with_missing(n, a=3, d=3):  # dummy for time complexity computation
    full = [a + i * d for i in range(n + 1)]
    miss = n // 2
    arr = full[:miss] + full[miss + 1:]
    return arr

if __name__ == "__main__": #
    arr = [3, 6, 9, 12, 15, 21]
    missing_number = missing_in_ap(arr)
    print(missing_number)

    sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]  # time complexity calculation using various array sizes of n size
    print("n\tlog2(n)\truntime (s)")
    for n in sizes:
        arr = make_ap_with_missing(n)
        start = time.perf_counter()
        missing_in_ap(arr)
        end = time.perf_counter()
        runtime = end - start
        print(f"{n}\t{math.log2(n):.2f}\t{runtime:.8f}")
