import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr[:pivot_index] + arr[pivot_index+1:] if x <= pivot]
    right = [x for x in arr[:pivot_index] + arr[pivot_index+1:] if x > pivot]

    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)

def analyze_quick_sort(arr, variant="deterministic"):
    start_time = time.time()
    if variant == "deterministic":
        sorted_arr = quick_sort(arr)
    elif variant == "randomized":
        sorted_arr = randomized_quick_sort(arr)
    else:
        print("Invalid variant specified")
        return

    end_time = time.time()
    execution_time = end_time - start_time
    return sorted_arr, execution_time

# Test the analysis with a sample array
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr_det, time_det = analyze_quick_sort(arr, variant="deterministic")
sorted_arr_rand, time_rand = analyze_quick_sort(arr, variant="randomized")

print("Deterministic Quick Sort:")
print("Sorted Array:", sorted_arr_det)
print("Execution Time: {:.6f} seconds".format(time_det))

print("\nRandomized Quick Sort:")
print("Sorted Array:", sorted_arr_rand)
print("Execution Time: {:.6f} seconds".format(time_rand))