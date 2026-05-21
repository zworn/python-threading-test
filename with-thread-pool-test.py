from concurrent.futures import ThreadPoolExecutor
import time

def worker(name, delay):
    print(f"[{name}] starting")
    time.sleep(delay)
    print(f"[{name}] done after {delay}s")

tasks = [("thread-a", 3), ("thread-b", 1), ("thread-c", 2)]

start_time = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    for name, delay in tasks:
        executor.submit(worker, name, delay)

elapsed_time = time.time() - start_time
print(f"\n\nall done in {elapsed_time:.2f}s")
