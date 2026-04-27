import numpy as np
import time


print("--- Task 1: Temperature Conversion ---")
temps_celsius = np.array([22, 25, 28, 24, 26])


temps_fahrenheit = temps_celsius * 1.8 + 32
avg_f = np.mean(temps_fahrenheit)

print(f"Celsius: {temps_celsius}")
print(f"Fahrenheit: {temps_fahrenheit}")
print(f"Average Fahrenheit: {avg_f:.1f}")



print("\n--- Task 2: Score Statistics ---")
scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

shape = scores.shape
total_elements = scores.size
highest = np.max(scores)
lowest = np.min(scores)
score_range = highest - lowest

print(f"Shape: {shape}")
print(f"Total elements: {total_elements}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Range: {score_range}")



print("\n--- Task 3: NumPy vs Python Performance ---")

n = 50000
np_arr = np.arange(1, n + 1)
py_list = list(range(1, n + 1))


start_np = time.time()
sum_np = np.sum(np_arr)
duration_np = time.time() - start_np


start_py = time.time()
sum_py = sum(py_list)
duration_py = time.time() - start_py


speed_factor = duration_py / duration_np

print(f"NumPy sum: {sum_np}")
print(f"Python sum: {sum_py}")
print(f"NumPy time: {duration_np:.4f} seconds")
print(f"Python time: {duration_py:.4f} seconds")
print(f"NumPy is {speed_factor:.1f}x faster")
