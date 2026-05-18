# Python Threading Test

A minimal demonstration of Python's `threading` module for running I/O-bound tasks concurrently.

## What It Does

Three tasks are defined, each with a name and a simulated delay:

| Task | Delay |
|------|-------|
| Thread-A | 3s |
| Thread-B | 1s |
| Thread-C | 2s |

Each task is assigned to a `threading.Thread`. All three threads start immediately, run in parallel, and the main program waits for all of them to finish via `.join()` before printing the total elapsed time.

## Expected Results

**Without threading** (sequential execution):

```
[Thread-A] Starting
[Thread-A] Done after 3s
[Thread-B] Starting
[Thread-B] Done after 1s
[Thread-C] Starting
[Thread-C] Done after 2s

All done in 6.00s
```

Total time = sum of all delays (3 + 1 + 2 = **6 seconds**).

---

**With threading** (concurrent execution):

```
[Thread-A] Starting
[Thread-B] Starting
[Thread-C] Starting
[Thread-B] Done after 1s
[Thread-C] Done after 2s
[Thread-A] Done after 3s

All done in 3.00s
```

Total time = longest single delay (**3 seconds**). The other tasks complete in the background while the slowest one runs.

> Print order within the "Starting" lines may vary slightly depending on OS thread scheduling.

## When This Pattern Applies

Threading in Python is effective for **I/O-bound** work — tasks that spend most of their time waiting rather than computing. The GIL (Global Interpreter Lock) limits true CPU parallelism for pure Python code, but it releases during I/O waits, making threads genuinely faster there.

Realistic examples where this pattern fits:

| Scenario | Example |
|----------|---------|
| HTTP API calls | Fetching data from multiple endpoints simultaneously |
| Database queries | Running independent queries against separate tables or databases |
| File I/O | Reading or writing multiple files concurrently |
| DNS resolution | Resolving a batch of hostnames in parallel |
| Email / messaging | Sending notifications to multiple recipients at once |
| External process calls | Running shell commands or subprocesses in parallel |
| Web scraping | Fetching and parsing multiple pages concurrently |

## When Not to Use This Pattern

- **CPU-bound tasks** (image processing, number crunching, ML inference): use `multiprocessing` or `concurrent.futures.ProcessPoolExecutor` instead, since they bypass the GIL.
- **Large-scale concurrency** (thousands of tasks): prefer `asyncio`, which handles many concurrent I/O tasks with a single thread and no OS thread overhead.

## Running

```bash
python python-threading-test.py
```
