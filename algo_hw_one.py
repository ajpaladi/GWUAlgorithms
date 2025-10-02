# algo_timings.py
import time
import math

# Range of n values to test
n_values = [
    10**1, 10**2, 10**3, 10**4, 10**5,
    10**6, 10**7, 10**8, 10**9, 10**10,
    10**11, 10**12, 10**13, 10**14, 10**15,
    10**16, 10**17, 10**18, 10**19, 10**20,
]

def algo(n: int):
    """Algorithm with O(log n * log log n) complexity."""
    j = 2
    while j < n:
        k = 2
        while k < n:
            _ = k & 1  # O(1) dummy work
            k = math.ceil(k * math.sqrt(k))  # growth step
        j += j // 2

def main():
    """Runs algo() for each n and records execution time."""
    print(f"{'n':>12} {'time_ms':>12}")
    print("-" * 25)
    for n in n_values:
        t0 = time.perf_counter()
        algo(n)
        t1 = time.perf_counter()
        print(f"{n:>12} {((t1 - t0) * 1000):>12.6f}")

if __name__ == "__main__":
    main()
