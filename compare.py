import random
import time
import copy
import statistics

# -----------------------------
# Sorting Algorithm Definitions
# -----------------------------

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# -----------------------------
# Experimental Parameters
# -----------------------------

input_sizes = [100, 500, 1000, 1500, 2000, 2500, 3000]
num_trials = 5  # Number of repeated runs per input size

results = []

# -----------------------------
# Experimental Procedure
# -----------------------------

for n in input_sizes:
    bubble_times = []
    merge_times = []

    for _ in range(num_trials):
        # Generate synthetic dataset
        original_list = [random.randint(0, 10000) for _ in range(n)]

        # Create identical copies
        bubble_list = copy.deepcopy(original_list)
        merge_list = copy.deepcopy(original_list)

        # Measure Bubble Sort execution time
        start_time = time.perf_counter()
        bubble_sort(bubble_list)
        end_time = time.perf_counter()
        bubble_times.append(end_time - start_time)

        # Measure Merge Sort execution time
        start_time = time.perf_counter()
        merge_sort(merge_list)
        end_time = time.perf_counter()
        merge_times.append(end_time - start_time)

    # Compute average execution times
    avg_bubble_time = statistics.mean(bubble_times)
    avg_merge_time = statistics.mean(merge_times)

    results.append((n, avg_bubble_time, avg_merge_time))

# -----------------------------
# Output Results
# -----------------------------

print("Input Size | Bubble Sort Avg Time (s) | Merge Sort Avg Time (s)")
print("-" * 60)

for row in results:
    print(f"{row[0]:>10} | {row[1]:>23.6f} | {row[2]:>23.6f}")


import matplotlib.pyplot as plt

# -----------------------------
# Prepare Data for Plotting
# -----------------------------

input_sizes = [row[0] for row in results]
bubble_times = [row[1] for row in results]
merge_times = [row[2] for row in results]

# -----------------------------
# Generate Line Plot
# -----------------------------

plt.figure(figsize=(8, 5))

plt.plot(input_sizes, bubble_times, marker='o', label='Bubble Sort')
plt.plot(input_sizes, merge_times, marker='o', label='Merge Sort')

plt.xlabel('Input Size (Number of Elements)')
plt.ylabel('Average Execution Time (Seconds)')
plt.title('Comparison of Bubble Sort and Merge Sort Execution Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
