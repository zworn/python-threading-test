import threading
import time

def worker(name, delay):
    print(f"[{name}] Starting")
    time.sleep(delay) # simulate some io work here
    print(f"[{name}] Done after {delay}s")

thread_list = []
tasks = [("Thread-A", 3), ("Thread-B", 1), ("Thread-C", 2)]

start_time = time.time()

for name, delay in tasks:
    thread = threading.Thread(target=worker, args=(name, delay))
    thread_list.append(thread)
    thread.start()

for thread in thread_list:
    thread.join()

elapsed_time = time.time() - start_time
print(f"\nAll done in {elapsed_time:.2f}s")
