import random
import statistics
results = []
for i in range(1, 1001):
    n1 = int(random.randint(1, 6))
    n2 = int(random.randrange(1,7))
    results.append(sum([n1,n2]))
mean = statistics.mean(results)
median = statistics.median(results)
mode = statistics.mode(results)

print("--- Simulation Results (1000 rolls) ---")
print(f"Mean:  {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Mode: {mode}")