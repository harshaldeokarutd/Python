import psutil
import os
import time

# Measure memory usage for List Approach
process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss  # Memory before

# Using List
numbers = [i for i in range(10000000)]

mem_after = process.memory_info().rss  # Memory after
print(f"Memory used by List: {mem_after - mem_before} bytes")

# Measure memory usage for Generator Approach
mem_before = process.memory_info().rss  # Memory before

# Using Generator
def number_generator():
    for i in range(10000000):
        yield i

gen = number_generator()

# Consume some values from the generator
for _ in range(100):  # Only consume 100 values, not all
    next(gen)

mem_after = process.memory_info().rss  # Memory after
print(f"Memory used by Generator: {mem_after - mem_before} bytes")
