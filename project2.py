import time
import math

def missing_in_ap(arr):
    n = len(arr)
    a = arr[0]
    d = (arr[-1] - arr[0]) / n
    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        expected = a + mid * d
        if arr[mid] == expected:
            lo = mid + 1
        else:
            hi = mid
    missing = a + lo * d
    return round(missing)

def make_ap_with_missing(n, a=3, d=3):
    full = [a + i * d for i in range(n + 1)]
    miss = n // 2
    arr = full[:miss] + full[miss + 1:]
    return arr

if __name__ == "__main__":
    arr = [3, 6, 9, 12, 15, 21]
    missing_number = missing_in_ap(arr)
    print(missing_number)

    sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]
    print("n\tlog2(n)\truntime (s)")
    for n in sizes:
        arr = make_ap_with_missing(n)
        start = time.perf_counter()
        missing_in_ap(arr)
        end = time.perf_counter()
        runtime = end - start
        print(f"{n}\t{math.log2(n):.2f}\t{runtime:.8f}")
