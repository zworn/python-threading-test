import threading
import time

def worker(name, delay):
    print(f"[{name}] starting")
    time.sleep(delay) # simulate some io work here
    print(f"[{name}] done after {delay}s")

thread_list = []
tasks = [("thread-a", 3), ("thread-b", 1), ("thread-c", 2)]

start_time = time.time()

for name, delay in tasks:
    thread = threading.Thread(target=worker, args=(name, delay))
    thread_list.append(thread)
    thread.start()

for thread in thread_list:
    thread.join()

elapsed_time = time.time() - start_time
print(f"\nall done in {elapsed_time:.2f}s")
