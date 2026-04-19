# Phase 0 — Planning the `asyncio` Roadmap ⚡

## Mental model

1. **Learn what `asyncio` actually is**
2. **Learn how the event loop thinks**
3. **Learn how async tasks are created, awaited, cancelled, and timed out**
4. **Learn where async beats threading, and where it absolutely does not**
5. **Practice notebook-first async patterns**
6. **Train for interview answers, bug reading, and design choices**

```text
Synchronous code
    └── one thing blocks everything

Threading
    └── many OS threads
        ├── good for blocking I/O with sync libraries
        └── shared-state + locks can get messy

Asyncio
    └── one event loop, many cooperative tasks
        ├── great for lots of waiting / network-style work
        └── terrible if you block the loop
```

---

## Exact phase count

I recommend **5 total phases**:

* **Phase 0** → planning
* **Phase 1** → async foundations
* **Phase 2** → real asyncio mechanics
* **Phase 3** → asyncio vs threading vs multiprocessing
* **Phase 4** → practical notebook labs + interview mastery

That keeps it **under 6**, but still complete enough for both **practical work** and **interviews**.

---

## What we are planning for

I’m treating “Ayscio” as **`asyncio`**. The official Python docs describe `asyncio` as Python’s library for writing concurrent code with `async` / `await`, and say it is often a strong fit for **I/O-bound** and **high-level structured network code**. Python’s conceptual overview also centers the mental model around the **event loop**, **coroutine functions/objects**, **tasks**, and `await`. ([Python documentation][1])

Because you’ll use **Jupyter notebooks**, I’ll teach this in a notebook-first way. IPython supports **top-level `await`** in interactive environments, so we’ll learn both notebook style and script style, without mixing them up and confusing the event loop model. ([IPython Documentation][2])

---

# The roadmap

## Phase 1 — Async foundations and notebook execution model

### What you’ll master

* what a **coroutine** is
* `async def` vs normal `def`
* what `await` really means
* what the **event loop** does
* coroutine object vs task
* notebook style:

  * top-level `await`
* script style:

  * `asyncio.run(...)`

### Why this phase comes first

If your mental model is weak here, everything later becomes memorization instead of understanding.

### Solved examples we’ll include

* “hello / world” with `await asyncio.sleep(...)`
* sequential vs concurrent async waiting
* notebook `await` vs script `asyncio.run(...)`

### Similar exercises

* predict which code runs sequentially
* fix “forgot to await” mistakes
* convert sync-looking code into correct coroutine flow

### Interview focus

* What is `asyncio`?
* What is a coroutine?
* What does `await` do?
* What is the event loop?

---

## Phase 2 — Real asyncio mechanics: tasks, cancellation, timeouts, queues, and blocking-code traps

### What you’ll master

* creating tasks
* `asyncio.gather(...)`
* **`TaskGroup`**
* cancellation
* timeouts
* graceful cleanup
* async queues
* semaphores / rate limiting
* producer-consumer in async style
* the biggest async bug:

  * **blocking the event loop**

Python’s current high-level docs explicitly cover coroutines/tasks, task groups, timeouts, queues, synchronization primitives, and subprocesses, so we’ll stay on those modern high-level APIs instead of going low-level too early. ([Python documentation][3])

The official docs also note that asyncio synchronization primitives and queues are **not thread-safe**, which is important because this phase will teach you not to mentally mix `threading` tools and `asyncio` tools. ([Python documentation][4])

### Solved examples we’ll include

* fan-out / fan-in async requests
* cancellation with cleanup
* timeout-wrapped work
* async queue worker pipeline
* rate limiting with semaphore

### Similar exercises

* fix an event-loop-blocking bug
* add timeout and retry behavior
* convert a threaded queue example into an async queue version

### Interview focus

* What is a task?
* `gather` vs `TaskGroup`
* How does cancellation work?
* Why is blocking the event loop so dangerous?

---

## Phase 3 — Asyncio vs threading vs multiprocessing: where each shines, and where each hurts

### This is the phase you explicitly asked for

Here we’ll answer:

* what async solves that threading struggles with
* when threading is cleaner than async
* when neither is the right answer
* how to bridge async code with blocking code

Python’s docs say `asyncio` is often a fit for I/O-bound, structured network work, and they also warn that **blocking code should not be called directly** in the event loop. The docs recommend offloading blocking work with `run_in_executor()` and support using other OS threads or processes for that. ([Python documentation][5])

### What async often does better

* large numbers of mostly-waiting tasks
* central control of cancellation and timeouts
* less lock-heavy shared-state reasoning
* async-native network/database stacks

### Where threading is often better

* existing **blocking** libraries
* incremental adoption in sync codebases
* background integration with code that is not async-native

### Where pure asyncio is a bad fit

* blocking calls inside coroutines
* CPU-heavy work as the main workload
* ecosystems where the library stack is mostly synchronous

### Where threading is a bad fit

* huge fan-out of mostly-idle I/O tasks when thread count and shared-state complexity start hurting simplicity or scalability

### Where neither is the answer

* CPU-bound Python workloads
* that usually moves the conversation toward **multiprocessing** or native/vectorized tools

### Solved examples we’ll include

* same workload in:

  * sync
  * threading
  * asyncio
* blocking function inside coroutine: why everything stalls
* using threads/executors to bridge blocking work into async code

### Similar exercises

* classify workloads:

  * async
  * threading
  * multiprocessing
* explain why a bad choice is bad
* rewrite a blocking async example correctly

### Interview focus

* Async vs threading?
* Async vs multiprocessing?
* When does threading fail and async shine?
* When does async fail and threading win?

---

## Phase 4 — Practical notebook labs + interview mastery

### What you’ll master

* writing clean async code in notebooks
* avoiding notebook/event-loop confusion
* real async workflow patterns
* converting hands-on work into interview answers

### Labs we’ll include

* async fake API batch runner
* async producer-consumer pipeline
* bounded async queue / backpressure
* rate-limited crawler or fetcher
* graceful cancellation lab
* async + blocking library bridge lab

### Interview prep we’ll include

* 30-second answers
* 90-second answers
* bug-reading drills
* design-choice drills
* async vs thread decision drills

### Why this final phase matters

This is where knowledge becomes **usable**:

* usable in notebooks
* usable in work
* usable in interviews

---

# Standard structure for every phase

To keep the learning consistent and ADHD-friendly, every phase will use the same frame:

## Each phase will include

* **Theory with lots of pointers**
* **2 solved notebook examples**
* **3 similar exercises**
* **1 comparison drill**
* **1 interview drill**
* **1 recap sheet**

That gives repetition without turning the topic into a wall of text.

---

# Notebook plan

## Suggested notebook files

```text
00_asyncio_plan.ipynb
01_async_foundations.ipynb
02_async_tasks_cancellation_queues.ipynb
03_async_vs_threading_vs_multiprocessing.ipynb
04_async_practical_labs_and_interviews.ipynb
```

## Internal section template for each notebook

```text
1. Goal
2. Mental model
3. Theory pointers
4. Diagram
5. Solved example 1
6. Solved example 2
7. Similar exercises
8. Interview drill
9. Recap
```

---

# What we will intentionally *not* overfocus on early

We will **not** spend early time on low-level transports/protocols or framework-author internals. The current Python docs explicitly position those low-level transport/protocol APIs as something mainly for **libraries and frameworks**, not typical high-level application code. ([Python documentation][6])

That means the roadmap will stay focused on the stuff you’ll actually use and get interviewed on first:

* coroutines
* tasks
* cancellation
* queues
* semaphores
* timeouts
* task groups
* blocking-code boundaries
* tool choice

---

# The key promise of this roadmap

## By the end, you should be able to

* explain `asyncio` simply
* write correct notebook-first async code
* avoid blocking the event loop
* use async queues, timeouts, cancellation, and task groups properly
* explain when **async wins**
* explain when **threading wins**
* explain when **multiprocessing** is the real answer
* answer interview questions with real examples instead of vague theory

---

# Final roadmap snapshot

```text
Phase 0  -> Planning
Phase 1  -> Async foundations + event loop + notebook model
Phase 2  -> Tasks, TaskGroup, cancellation, timeouts, queues, semaphores
Phase 3  -> Async vs threading vs multiprocessing
Phase 4  -> Practical labs + interview mastery
```

---

# Best next move

Next I’d take you into **Phase 1 — Async foundations and notebook execution model**.

[1]: https://docs.python.org/3/library/asyncio.html?utm_source=chatgpt.com "asyncio — Asynchronous I/O — Python 3.14.4 documentation"
[2]: https://ipython.readthedocs.io/en/stable/interactive/autoawait.html?utm_source=chatgpt.com "Asynchronous in REPL: Autoawait — IPython 9.12.0 documentation"
[3]: https://docs.python.org/3/library/asyncio-task.html?utm_source=chatgpt.com "Coroutines and tasks — Python 3.14.3 documentation"
[4]: https://docs.python.org/3/library/asyncio-sync.html?utm_source=chatgpt.com "Synchronization Primitives — Python 3.14.4 documentation"
[5]: https://docs.python.org/3/library/asyncio-dev.html?utm_source=chatgpt.com "Developing with asyncio — Python 3.14.4 documentation"
[6]: https://docs.python.org/3/library/asyncio-protocol.html?utm_source=chatgpt.com "Transports and Protocols — Python 3.14.4 documentation"


# Phase 1 — Async Foundations & Event Loop 🧠⚡

---

## Mental model for this phase

1. **What problem async solves**
2. **What a coroutine is**
3. **What `async` / `await` actually do**
4. **How the event loop works**
5. **Why async is cooperative (not parallel)**
6. **How execution really flows**
7. **Jupyter vs script execution model**
8. **Solved examples**
9. **Exercises**
10. **Interview-ready answers**

---

# 1) Goal of Phase 1

By the end of this phase, you should be able to:

* explain **what asyncio is solving**
* understand **coroutines vs functions**
* understand **`await` = suspension point**
* explain **event loop in simple terms**
* predict execution order of async code
* run async code correctly in **Jupyter**
* avoid the **#1 beginner mistake**: “why didn’t my async function run?”

---

# 2) The core problem async solves

## Problem

In synchronous code:

```text
Do task A → wait → do task B → wait → do task C
```

If task A is waiting (network/file/etc), **everything is stuck**

---

## Async idea

```text
Start task A
While A waits → do B
While B waits → do C
```

---

## Visual

```text
Time →
Task A: [wait------]
Task B:     [wait------]
Task C:         [wait------]

All overlap WITHOUT threads
```

---

## Key insight

> Async is about **efficient waiting**, not parallel execution.

---

# 3) What is a coroutine?

## Simple definition

A **coroutine** is a function that can:

* pause execution
* give control back
* resume later

---

## Syntax

```python
async def my_func():
    pass
```

---

## Important distinction

| Type            | Meaning                          |
| --------------- | -------------------------------- |
| normal function | runs immediately                 |
| async function  | returns a coroutine object       |
| coroutine       | needs to be awaited or scheduled |

---

## CRITICAL rule 🚨

```python
async def f():
    print("hello")

f()   # DOES NOT RUN
```

You just created a coroutine object.

---

## Correct execution

```python
await f()
```

---

## Mental model

```text
async def → creates a plan
await → executes the plan
```

---

# 4) What does `await` actually do?

## Core idea

> `await` means: “pause here and let something else run”

---

## Example

```python
await asyncio.sleep(2)
```

This means:

* do NOT block everything
* suspend this coroutine
* let event loop run other tasks

---

## Visual

```text
Coroutine A:
  start → await → paused

Event loop:
  picks another coroutine
```

---

## Key insight

> `await` is where concurrency happens

---

# 5) The event loop (heart of asyncio)

## Simple definition

The **event loop** is:

> a scheduler that runs and switches between coroutines

---

## Mental model

```text
Event Loop:
    while tasks exist:
        run until a task hits await
        switch to next task
```

---

## Visual

```text
Loop:
  run A → A hits await → pause
  run B → B hits await → pause
  run C → C hits await → pause
  resume A → ...
```

---

## Key property

* only ONE coroutine runs at a time
* switching happens ONLY at `await`

---

## Important conclusion

> Async is NOT parallel
> Async is **cooperative multitasking**

---

# 6) Async vs threading (early intuition)

| Feature    | Threading              | Async                 |
| ---------- | ---------------------- | --------------------- |
| Execution  | OS-controlled          | event-loop controlled |
| Switching  | preemptive             | cooperative           |
| Complexity | locks, race conditions | structured flow       |
| Best for   | blocking code          | async I/O             |

---

## Key difference

* Threads: system interrupts you
* Async: you decide when to yield (`await`)

---

# 7) Solved Example 1 — Sequential vs async

## Code

```python
import asyncio
import time

async def task(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)
    print(f"{name} end")

async def main():
    await task("A", 2)
    await task("B", 2)

start = time.time()
await main()
print("Time:", time.time() - start)
```

---

## What happens

```text
A start
(wait 2s)
A end
B start
(wait 2s)
B end
Total ≈ 4 seconds
```

---

## Why?

Because:

```python
await task(...)
await task(...)
```

means **sequential execution**

---

# 8) Solved Example 2 — True async concurrency

## Code

```python
import asyncio
import time

async def task(name, delay):
    print(f"{name} start")
    await asyncio.sleep(delay)
    print(f"{name} end")

async def main():
    t1 = asyncio.create_task(task("A", 2))
    t2 = asyncio.create_task(task("B", 2))

    await t1
    await t2

start = time.time()
await main()
print("Time:", time.time() - start)
```

---

## Output

```text
A start
B start
(wait 2s)
A end
B end
Total ≈ 2 seconds
```

---

## Key difference

```python
create_task() → schedules work concurrently
await → waits for result
```

---

## Mental model

```text
create_task → register with event loop
await → wait for completion
```

---

# 9) Async execution flow diagram

```text
main()
  │
  ├── create_task(A)
  ├── create_task(B)
  │
  ├── await A
  │       ├── A runs → await sleep → pause
  │       ├── B runs → await sleep → pause
  │       ├── resume A
  │       └── resume B
  │
  └── await B
```

---

# 10) Jupyter vs script execution

## In Jupyter ✅

You can directly do:

```python
await main()
```

---

## In Python script ❌

You must do:

```python
asyncio.run(main())
```

---

## Why difference?

* Jupyter already runs an event loop
* script needs to start one

---

## Common mistake 🚨

```python
asyncio.run(main())   # ❌ inside Jupyter → error
```

---

## Rule

| Environment | Run async             |
| ----------- | --------------------- |
| Jupyter     | `await main()`        |
| Script      | `asyncio.run(main())` |

---

# 11) Core async mistakes (Phase 1 level)

## Mistake 1 — forgetting `await`

```python
task()   # does nothing
```

---

## Mistake 2 — thinking async = automatic concurrency

```python
await f()
await g()
```

Still sequential.

---

## Mistake 3 — no `create_task()`

No scheduling → no concurrency.

---

## Mistake 4 — assuming parallelism

Async ≠ multi-core execution.

---

# 12) Similar exercises

---

## Exercise 1 — predict output order

Write:

```python
async def f():
    print("A")
    await asyncio.sleep(1)
    print("B")

async def g():
    print("C")
    await asyncio.sleep(1)
    print("D")
```

### Try:

```python
await f()
await g()
```

Then:

```python
t1 = asyncio.create_task(f())
t2 = asyncio.create_task(g())
await t1
await t2
```

### Question

* How does output differ?
* Why?

---

## Exercise 2 — missing await bug

```python
async def hello():
    print("hello")

hello()
```

### Fix it correctly

---

## Exercise 3 — timing difference

* run sequential version
* run concurrent version

### Measure time difference

---

## Exercise 4 — mental model

Answer:

* What does `await` do?
* What does `create_task` do?

---

# 13) Mini challenge

## Problem

You have 3 API calls:

* each takes 2 seconds
* you want total time ≈ 2 seconds

### Questions

* Should you use `await f(); await g(); await h()`?
* What should you use instead?

---

## Answer

* No → sequential
* Use:

  * `create_task`
  * or later `gather()`

---

# 14) Interview mastery (Phase 1)

---

## Question 1 — What is asyncio?

### Strong answer

> Asyncio is Python’s framework for writing concurrent code using a single-threaded event loop and coroutines. It is especially useful for I/O-bound tasks where programs spend time waiting.

---

## Question 2 — What is a coroutine?

### Strong answer

> A coroutine is a function defined with `async def` that can pause and resume execution using `await`. It allows cooperative multitasking within the event loop.

---

## Question 3 — What does `await` do?

### Strong answer

> `await` pauses the current coroutine and gives control back to the event loop so other tasks can run. It marks a suspension point.

---

## Question 4 — Why doesn’t async function run immediately?

### Strong answer

> Calling an async function returns a coroutine object. It only runs when awaited or scheduled using something like `create_task()`.

---

## Question 5 — Is asyncio parallel?

### Strong answer

> No, asyncio is not parallel by default. It runs tasks cooperatively on a single thread and switches execution at `await` points.

---

# 15) How to answer clearly

## Best structure

```text
Definition
→ what it solves
→ example
→ limitation
```

---

## Example answer

> Asyncio is a concurrency model that uses a single-threaded event loop to run multiple tasks. It solves the problem of wasted time during I/O waits by switching tasks at `await` points. For example, multiple network calls can overlap without threads. However, it does not provide parallel CPU execution.

---

# 16) One-page cheat sheet

```text
async def
  -> defines coroutine

await
  -> pause and yield control

create_task()
  -> schedule concurrent execution

event loop
  -> runs and switches between coroutines

async != parallel
  -> cooperative concurrency

Jupyter
  -> use await

Script
  -> use asyncio.run()
```

---

# 17) Copy-ready notebook summary

```python
phase_1_summary = {
    "coroutine": "Function that can pause and resume",
    "await": "Suspends execution and yields control",
    "event loop": "Scheduler that runs coroutines",
    "create_task": "Schedules concurrent execution",
    "async vs parallel": "Async is cooperative, not parallel",
    "jupyter rule": "Use await directly",
    "script rule": "Use asyncio.run()"
}

for k, v in phase_1_summary.items():
    print(f"{k}: {v}")
```

---

# 18) Short recap

## You should now know

* coroutine ≠ function
* `await` = pause point
* event loop = scheduler
* async runs cooperatively
* concurrency requires `create_task`
* Jupyter execution rules

---

# 19) Next topics

## Phase 2 — Real Asyncio Mechanics

We will go deeper into:

1. `gather()` vs `create_task()`
2. `TaskGroup`
3. cancellation
4. timeouts
5. async queues
6. semaphores (rate limiting)
7. **BIG ONE: blocking the event loop**

---

# 20) Tiny self-test

Answer in 1–2 lines:

* What is a coroutine?
* What does `await` do?
* Why doesn’t calling async function run it?
* How do you run async code in Jupyter?
* Why is `create_task()` needed?
* Is asyncio parallel?

---

# Phase 2 — Asyncio in the Real World (Tasks, Cancellation, Queues, Timeouts) ⚙️⚡

---

## Mental model for this phase

1. **Coroutines don’t run → Tasks make them run**
2. **Concurrency = scheduling multiple tasks**
3. **You must control lifecycle (start, cancel, finish)**
4. **Async systems need flow control (queues, semaphores)**
5. **Biggest danger: blocking the event loop**
6. **Async ≠ magic → you must design it correctly**

---

# 1) Goal of Phase 2

By the end of this phase, you should be able to:

* create and manage **tasks properly**
* use:

  * `asyncio.create_task`
  * `asyncio.gather`
  * `TaskGroup`
* handle:

  * cancellation
  * timeouts
* build:

  * async producer-consumer pipelines
* avoid:

  * blocking the event loop (VERY IMPORTANT 🚨)
* explain async execution clearly in interviews

---

# 2) From coroutines → tasks

## Core idea

```text
Coroutine = recipe
Task = cooking happening right now
```

---

## Why tasks matter

Without tasks:

```python
await f()
await g()
```

➡️ sequential

---

With tasks:

```python
t1 = asyncio.create_task(f())
t2 = asyncio.create_task(g())
await t1
await t2
```

➡️ concurrent

---

## Key rule

> `create_task()` = “start running this coroutine concurrently”

---

# 3) Solved Example 1 — `create_task` vs sequential

```python
import asyncio
import time

async def work(name):
    print(f"{name} start")
    await asyncio.sleep(2)
    print(f"{name} end")

async def main():
    # concurrent
    t1 = asyncio.create_task(work("A"))
    t2 = asyncio.create_task(work("B"))

    await t1
    await t2

start = time.time()
await main()
print("Time:", time.time() - start)
```

---

## What happens

```text
A start
B start
(wait)
A end
B end
≈ 2 seconds
```

---

## Key insight

```text
create_task → register with event loop
await → wait for result
```

---

# 4) `asyncio.gather()` — simpler concurrency

## Problem with tasks

Too much manual handling.

---

## Solution

```python
await asyncio.gather(f(), g(), h())
```

---

## Solved Example 2

```python
async def task(n):
    await asyncio.sleep(1)
    return n * 2

results = await asyncio.gather(task(1), task(2), task(3))
print(results)
```

---

## Output

```text
[2, 4, 6]
```

---

## Key features

* runs all concurrently
* returns results in order
* fails fast (important nuance)

---

## Interview line

> `gather` is useful for running multiple independent coroutines concurrently and collecting their results.

---

# 5) `TaskGroup` (modern structured concurrency)

## Why introduced

Better error handling + structured lifecycle.

---

## Solved Example 3

```python
import asyncio

async def task(n):
    await asyncio.sleep(1)
    print(f"Task {n}")

async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(3):
            tg.create_task(task(i))

await main()
```

---

## Why better than `gather`

* automatic cancellation on failure
* structured block
* safer for real systems

---

## Interview line

> `TaskGroup` provides structured concurrency and better error handling compared to `gather`.

---

# 6) Cancellation — stopping tasks properly

## Why important

* long-running systems
* shutdown handling
* timeouts
* error recovery

---

## Solved Example 4

```python
import asyncio

async def worker():
    try:
        while True:
            print("Working...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Cleanup before exit")
        raise

async def main():
    t = asyncio.create_task(worker())
    await asyncio.sleep(2)
    t.cancel()
    await t

await main()
```

---

## Key concept

```text
cancel() → raises CancelledError inside coroutine
```

---

## Rule

> Always handle cancellation cleanly if resources are involved

---

# 7) Timeouts — avoid infinite waiting

## Problem

```text
Task never finishes → system hangs
```

---

## Solution

```python
await asyncio.wait_for(task(), timeout=2)
```

---

## Solved Example 5

```python
import asyncio

async def slow():
    await asyncio.sleep(5)

try:
    await asyncio.wait_for(slow(), timeout=2)
except asyncio.TimeoutError:
    print("Timed out")
```

---

## Key idea

* wraps coroutine
* cancels if timeout exceeded

---

## Interview line

> Timeouts prevent indefinite waiting and improve system resilience.

---

# 8) Async queues — producer-consumer

## Why needed

Avoid shared-state complexity.

---

## Pattern

```text
Producer → Queue → Consumers
```

---

## Solved Example 6

```python
import asyncio

queue = asyncio.Queue()

async def producer():
    for i in range(5):
        await queue.put(i)
        print(f"Produced {i}")
    await queue.put(None)

async def consumer():
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed {item}")

await asyncio.gather(producer(), consumer())
```

---

## Key insight

* `await queue.get()` → waits safely
* no locks needed
* clean coordination

---

## Interview line

> Async queues provide safe communication between coroutines without shared-state locking.

---

# 9) Semaphores — limit concurrency

## Problem

Too many concurrent tasks:

* API limits
* DB limits

---

## Solution

```python
sem = asyncio.Semaphore(3)
```

---

## Solved Example 7

```python
import asyncio

sem = asyncio.Semaphore(2)

async def worker(n):
    async with sem:
        print(f"Start {n}")
        await asyncio.sleep(2)
        print(f"End {n}")

await asyncio.gather(*(worker(i) for i in range(5)))
```

---

## What happens

* only 2 run at a time

---

## Interview line

> Semaphores limit concurrent access and help with rate limiting.

---

# 10) 🚨 The BIGGEST mistake: blocking the event loop

## What NOT to do

```python
import time

async def bad():
    time.sleep(2)   # ❌ BLOCKS EVERYTHING
```

---

## Why this is bad

```text
Event loop can't switch → everything freezes
```

---

## Correct version

```python
await asyncio.sleep(2)
```

---

## Real-world problem

```text
Blocking DB call
Blocking HTTP client
Heavy CPU computation
```

---

## Fix patterns

* use async libraries
* or offload:

```python
await loop.run_in_executor(...)
```

---

## Interview killer line

> Blocking the event loop defeats asyncio completely because no other tasks can run.

---

# 11) Execution flow diagram

```text
create_task(A)
create_task(B)

Event Loop:
  run A → await → pause
  run B → await → pause
  resume A
  resume B
```

---

# 12) Common mistakes

## Mistake 1 — forgetting await

```python
queue.put(x)   # ❌ should be await
```

---

## Mistake 2 — blocking calls inside async

```python
time.sleep()  ❌
```

---

## Mistake 3 — no cancellation handling

---

## Mistake 4 — spawning tasks but never awaiting

```python
asyncio.create_task(f())  # lost task
```

---

## Mistake 5 — using threading primitives in asyncio

Wrong mental model.

---

# 13) Similar exercises

---

## Exercise 1 — gather vs sequential

Compare:

```python
await f()
await g()
```

vs

```python
await asyncio.gather(f(), g())
```

---

## Exercise 2 — cancellation

* create infinite loop worker
* cancel after 2 seconds
* handle cleanup

---

## Exercise 3 — timeout

* wrap slow task with timeout
* handle exception

---

## Exercise 4 — queue pipeline

* 1 producer
* 2 consumers
* stop using sentinel

---

## Exercise 5 — semaphore

* limit to 3 concurrent tasks
* print order

---

# 14) Mini challenge

## Problem

You have 10 API calls:

* each takes 2 seconds
* max 3 allowed concurrently
* timeout = 3 seconds

### What tools?

### Answer

* `Semaphore(3)`
* `gather` or `TaskGroup`
* `wait_for`

---

# 15) Interview mastery

---

## Question — What is a task?

> A task is a wrapper around a coroutine that schedules it to run in the event loop.

---

## Question — gather vs TaskGroup?

> `gather` is simpler for collecting results, while `TaskGroup` provides structured concurrency and better failure handling.

---

## Question — why is blocking bad?

> Blocking stops the event loop, preventing all other tasks from running.

---

## Question — how do you cancel tasks?

> By calling `task.cancel()`, which raises `CancelledError` inside the coroutine.

---

## Question — why use async queue?

> To safely pass work between coroutines without shared-state complexity.

---

# 16) One-page cheat sheet

```text
create_task() → start coroutine
gather() → run many + collect results
TaskGroup → structured concurrency

cancel() → stop task
wait_for() → timeout control

Queue → async producer-consumer
Semaphore → limit concurrency

BIG RULE:
Never block event loop
```

---

# 17) Copy-ready notebook summary

```python
phase_2_summary = {
    "task": "Running coroutine scheduled in event loop",
    "gather": "Run multiple coroutines concurrently",
    "TaskGroup": "Structured concurrency with better error handling",
    "cancel": "Stops task via CancelledError",
    "timeout": "Use wait_for to limit execution time",
    "queue": "Safe async communication",
    "semaphore": "Limits concurrency",
    "golden rule": "Never block the event loop"
}

for k, v in phase_2_summary.items():
    print(f"{k}: {v}")
```

---

# 18) Short recap

## You now understand

* tasks = running coroutines
* `gather` vs `TaskGroup`
* cancellation + cleanup
* timeouts
* async queues
* semaphores
* event loop blocking dangers

---

# 19) Next phase

## Phase 3 — Async vs Threading vs Multiprocessing 🔥

This is where you’ll learn:

* when async **beats threading**
* when threading **beats async**
* when both fail
* real-world decision making

---

# 20) Tiny self-test

Answer:

* What is a task?
* Why use `gather()`?
* What happens when you cancel a task?
* Why is blocking dangerous?
* When would you use a semaphore?
* What is async queue used for?

---

# Phase 3 — Async vs Threading vs Multiprocessing ⚔️⚡🧵

---

## Mental model for this phase

1. **Different tools solve different bottlenecks**
2. **Async = cooperative concurrency**
3. **Threading = OS-managed concurrency**
4. **Multiprocessing = true parallelism**
5. **Wrong tool = slow, buggy, or stuck system**
6. **Right tool = simple + scalable + correct**
7. **This phase is 80% interview gold**

---

# 1) Goal of Phase 3

By the end of this phase, you should be able to:

* explain **async vs threading vs multiprocessing**
* identify:

  * I/O-bound vs CPU-bound
* explain:

  * when async **shines**
  * when threading **wins**
  * when async **fails badly**
* choose the right tool in interviews confidently
* explain tradeoffs clearly (this is key 🔥)

---

# 2) The core decision framework

## First question always

```text
What is the bottleneck?
```

---

## Decision tree

```text id="p3_decision_tree"
Is work mostly waiting (I/O)?
  ├── Yes → async or threading
  │        ├── many tasks → asyncio
  │        └── blocking libs → threading
  │
  └── No (CPU heavy)
           → multiprocessing
```

---

# 3) Big picture comparison

| Feature         | Asyncio                | Threading                 | Multiprocessing |
| --------------- | ---------------------- | ------------------------- | --------------- |
| Execution model | single-threaded        | multi-threaded            | multi-process   |
| Switching       | cooperative (`await`)  | preemptive                | OS-level        |
| Best for        | I/O-bound (many tasks) | I/O-bound (blocking code) | CPU-bound       |
| Parallel CPU    | ❌                      | ❌ (GIL)                   | ✅               |
| Complexity      | medium                 | high (locks)              | high (IPC)      |
| Memory          | low                    | moderate                  | high            |

---

# 4) Asyncio shines when threading struggles

## Scenario 1 — MANY I/O tasks

### Example

```text id="p3_many_io"
10,000 HTTP requests
```

---

## Threading problem

* too many threads
* memory overhead
* context switching cost
* debugging chaos

---

## Async solution

```text id="p3_async_solution"
Single event loop
Thousands of tasks
Minimal overhead
```

---

## Key insight

> Async scales better when tasks are mostly waiting

---

## Interview line

> Asyncio shines when handling a large number of concurrent I/O-bound tasks because it avoids the overhead of creating and managing many threads.

---

# 5) Threading shines when async struggles

## Scenario 2 — blocking libraries

### Example

```text id="p3_blocking_lib"
Legacy DB driver
File I/O API
Third-party SDK (no async support)
```

---

## Async problem

```python
await blocking_call()  # ❌ blocks event loop
```

Everything freezes.

---

## Threading solution

```text id="p3_thread_solution"
Run blocking calls in threads
```

---

## Key insight

> Async only works if the ecosystem is async-friendly

---

## Interview line

> Threading is often better when working with blocking libraries that are not designed for async, because async code cannot safely call blocking operations.

---

# 6) When async FAILS badly 🚨

## Case 1 — blocking inside async

```python
async def bad():
    time.sleep(5)   # ❌ kills concurrency
```

---

## What happens

```text id="p3_block_event_loop"
Event loop stops → all tasks freeze
```

---

## Case 2 — CPU-heavy work

```python
async def compute():
    for i in range(10**9):
        pass
```

---

## Problem

* no `await`
* event loop never gets control back

---

## Key insight

> Async requires cooperative yielding (`await`)

---

## Interview line

> Asyncio fails when tasks block the event loop or perform CPU-heavy work without yielding.

---

# 7) When threading FAILS badly

## Case 1 — too many threads

```text id="p3_threads_fail"
Thousands of threads
→ memory blow-up
→ context switching overhead
```

---

## Case 2 — shared state complexity

* race conditions
* deadlocks
* locks everywhere

---

## Case 3 — debugging nightmare

* timing-dependent bugs
* non-deterministic behavior

---

## Key insight

> Threads introduce complexity via shared state

---

## Interview line

> Threading can become complex due to shared-state synchronization, and it does not scale well to very large numbers of concurrent tasks.

---

# 8) When BOTH async and threading fail

## Case — CPU-bound Python

```python
for i in range(10**9):
    do_work()
```

---

## Problem

* async: blocks event loop
* threads: GIL prevents parallelism

---

## Solution

```text id="p3_multiprocessing"
multiprocessing
```

---

## Key insight

> CPU-bound Python needs multiprocessing

---

## Interview line

> For CPU-bound workloads in Python, multiprocessing is preferred because it can use multiple CPU cores without being limited by the GIL.

---

# 9) Side-by-side example comparison

---

## Problem

3 tasks, each takes 2 seconds (I/O wait)

---

## Sync version

```text
A → wait → B → wait → C → wait
Total = 6s
```

---

## Threading

```text
A || B || C
Total ≈ 2s
```

---

## Async

```text
A || B || C
Total ≈ 2s (more scalable)
```

---

## CPU-bound version

```text
Threading → still slow (GIL)
Async → blocked
Multiprocessing → fast
```

---

# 10) Hybrid pattern (real-world important)

## Async + threads

```python
await loop.run_in_executor(...)
```

---

## Why needed

* async app
* but must call blocking function

---

## Example use

* legacy DB call
* file system operation
* CPU offload

---

## Interview line

> In async systems, blocking work can be offloaded to threads using executors to avoid blocking the event loop.

---

# 11) Execution model comparison diagram

```text id="p3_execution_model"
THREADING:
  OS switches threads anytime

ASYNC:
  switch only at await

MULTIPROCESS:
  separate processes run independently
```

---

# 12) Common decision mistakes

---

## Mistake 1 — using async for CPU work

Wrong tool.

---

## Mistake 2 — using threads for 10k tasks

Doesn't scale well.

---

## Mistake 3 — blocking inside async

Breaks everything.

---

## Mistake 4 — using multiprocessing for simple I/O

Overkill.

---

## Mistake 5 — ignoring ecosystem

If libraries are sync → async becomes painful.

---

# 13) Solved Example — blocking vs async

## Bad async

```python
import time

async def bad():
    time.sleep(2)  # ❌
```

---

## Good async

```python
await asyncio.sleep(2)
```

---

## Thread bridge

```python
await loop.run_in_executor(None, blocking_func)
```

---

# 14) Similar exercises

---

## Exercise 1 — classify workload

Choose best tool:

* 100 HTTP requests
* image processing loop
* DB calls using sync library
* 10k websocket connections

---

## Exercise 2 — fix bad async

```python
async def f():
    requests.get(url)  # ❌
```

Fix it.

---

## Exercise 3 — reasoning

Why is this bad?

```python
async def f():
    for i in range(10**9):
        pass
```

---

## Exercise 4 — compare tools

Write 3 lines explaining:

* async vs threading
* threading vs multiprocessing

---

# 15) Mini challenge

## Problem

You are building:

* web crawler
* thousands of URLs
* rate limit = 10
* parsing HTML (light CPU)
* using async HTTP library

### What to use?

### Answer

* asyncio
* semaphore for rate limit
* async tasks

---

## Twist

HTML parsing becomes heavy CPU.

### What changes?

* offload parsing → thread or process
* hybrid design

---

# 16) Interview mastery

---

## Question — Async vs threading?

### Strong answer

> Asyncio uses a single-threaded event loop and cooperative multitasking, while threading uses OS-managed threads. Async is better for large-scale I/O-bound concurrency, while threading is more suitable when working with blocking libraries.

---

## Question — When does async shine?

> Async shines when handling many concurrent I/O-bound tasks, especially when using async-native libraries.

---

## Question — When does async fail?

> Async fails when tasks block the event loop or when performing CPU-heavy work without yielding.

---

## Question — When is threading better?

> Threading is better when using blocking APIs or integrating with libraries that are not async-compatible.

---

## Question — Async vs multiprocessing?

> Async handles I/O concurrency efficiently, while multiprocessing is used for CPU-bound parallelism across cores.

---

# 17) How to answer clearly

## Best structure

```text
Workload type
→ bottleneck
→ best tool
→ why
→ limitation
```

---

## Example

> For many HTTP requests, I would use asyncio because the bottleneck is I/O waiting. It allows thousands of concurrent tasks with low overhead. However, if the workload becomes CPU-heavy, I would switch to multiprocessing.

---

# 18) One-page cheat sheet

```text id="p3_cheatsheet"
ASYNC
  → many I/O tasks
  → async libraries required
  → fails if blocking

THREADING
  → blocking I/O
  → simpler integration
  → shared-state complexity

MULTIPROCESSING
  → CPU-bound work
  → true parallelism
  → higher overhead
```

---

# 19) Copy-ready notebook summary

```python
phase_3_summary = {
    "async": "Best for many I/O-bound tasks",
    "threading": "Best for blocking I/O",
    "multiprocessing": "Best for CPU-bound work",
    "async fails": "Blocking or CPU-heavy tasks",
    "threading fails": "Too many threads or shared-state complexity",
    "best practice": "Choose based on bottleneck"
}

for k, v in phase_3_summary.items():
    print(f"{k}: {v}")
```

---

# 20) Short recap

## You now understand

* async vs threading vs multiprocessing
* when each shines
* when each fails
* how to choose correctly
* how to explain decisions in interviews

---

# 21) Final phase next

## Phase 4 — Practical Labs + Interview Mastery 🚀

We’ll combine everything:

* real async pipelines
* rate-limited crawlers
* async queues
* hybrid designs
* interview drills

---

# 22) Tiny self-test

Answer clearly:

* When should you use asyncio?
* When should you use threading instead?
* Why does async fail with blocking code?
* Why doesn’t threading speed up CPU tasks?
* What is the best tool for CPU-bound Python?
* What is the biggest async mistake?

---

# Phase 4 — Practical Async Labs + Interview Mastery 🚀⚡

---

## Mental model for this phase

1. **Async becomes real only when you build systems**
2. **You must manage flow, limits, and shutdown**
3. **Async ≠ just `await` → it’s architecture**
4. **Most bugs = blocking, missing awaits, bad cancellation**
5. **You need stories for interviews, not just definitions**

---

# 1) Goal of Phase 4

By the end of this phase, you should be able to:

* build **real async workflows**
* use:

  * tasks
  * queues
  * semaphores
  * timeouts
* design:

  * pipelines
  * rate-limited systems
  * graceful shutdown
* debug async code confidently
* answer interview questions using **real examples**

---

# 2) Lab roadmap (what we’ll build)

We’ll do **5 high-value labs**:

1. **Async API batch runner**
2. **Rate-limited async crawler**
3. **Async producer-consumer pipeline**
4. **Bounded queue (backpressure) system**
5. **Graceful shutdown + cancellation system**

Each lab includes:

* design
* code
* observations
* interview takeaway

---

# 3) Lab 1 — Async API batch runner

## Problem

You have many independent API calls.

## Best design

* `asyncio.gather`
* async tasks

---

## Code

```python
import asyncio
import random

async def fake_api(id):
    delay = random.uniform(1, 3)
    print(f"API {id} start ({delay:.1f}s)")
    await asyncio.sleep(delay)
    print(f"API {id} done")
    return f"result-{id}"

async def main():
    results = await asyncio.gather(*(fake_api(i) for i in range(5)))
    print("Results:", results)

await main()
```

---

## What to observe

* all APIs start immediately
* finish order varies
* results stay ordered

---

## Interview takeaway

> For independent I/O tasks, I use `gather()` to run them concurrently and collect results.

---

# 4) Lab 2 — Rate-limited async crawler

## Problem

* many requests
* max concurrency = 3

---

## Solution

* `Semaphore`

---

## Code

```python
import asyncio

sem = asyncio.Semaphore(3)

async def fetch(i):
    async with sem:
        print(f"Fetching {i}")
        await asyncio.sleep(2)
        print(f"Done {i}")

await asyncio.gather(*(fetch(i) for i in range(6)))
```

---

## What to observe

* only 3 tasks run at once

---

## Interview takeaway

> I use semaphores in async systems to enforce rate limits or control concurrency.

---

# 5) Lab 3 — Async producer-consumer pipeline

## Problem

* tasks arrive dynamically
* multiple workers process them

---

## Solution

* `asyncio.Queue`

---

## Code

```python
import asyncio

queue = asyncio.Queue()

async def producer():
    for i in range(5):
        await queue.put(i)
        print(f"Produced {i}")
    await queue.put(None)

async def consumer(name):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"{name} processing {item}")
        await asyncio.sleep(1)

await asyncio.gather(producer(), consumer("C1"))
```

---

## What to observe

* consumer waits safely
* no locks needed

---

## Interview takeaway

> Async queues provide structured communication without shared-state complexity.

---

# 6) Lab 4 — Bounded queue (backpressure)

## Problem

Producer is faster than consumer.

---

## Solution

```python
queue = asyncio.Queue(maxsize=2)
```

---

## Code

```python
import asyncio

queue = asyncio.Queue(maxsize=2)

async def producer():
    for i in range(5):
        print(f"Producing {i}")
        await queue.put(i)
        print(f"Produced {i}")

async def consumer():
    for _ in range(5):
        item = await queue.get()
        print(f"Consumed {item}")
        await asyncio.sleep(2)

await asyncio.gather(producer(), consumer())
```

---

## What to observe

* producer blocks when queue is full

---

## Interview takeaway

> Bounded queues apply backpressure and prevent uncontrolled growth.

---

# 7) Lab 5 — Graceful shutdown system

## Problem

* long-running worker
* needs clean exit

---

## Solution

* cancellation

---

## Code

```python
import asyncio

async def worker():
    try:
        while True:
            print("Working...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Cleanup done")
        raise

async def main():
    task = asyncio.create_task(worker())
    await asyncio.sleep(3)
    task.cancel()
    await task

await main()
```

---

## What to observe

* worker exits cleanly
* cleanup runs

---

## Interview takeaway

> I handle shutdown using cancellation and ensure cleanup logic runs.

---

# 8) Combined system (mini project)

## Problem

* producer creates jobs
* workers process jobs
* limit concurrency
* collect results
* shutdown cleanly

---

## Code

```python
import asyncio

queue = asyncio.Queue()
sem = asyncio.Semaphore(2)

async def producer():
    for i in range(6):
        await queue.put(i)
    for _ in range(2):
        await queue.put(None)

async def worker(name):
    while True:
        item = await queue.get()
        if item is None:
            break
        async with sem:
            print(f"{name} processing {item}")
            await asyncio.sleep(1)

await asyncio.gather(producer(), worker("W1"), worker("W2"))
```

---

## What this teaches

* queue + semaphore + tasks
* real-world async architecture

---

# 9) Debugging async systems

## Checklist

```text
Is nothing running?
  → forgot await

Is everything stuck?
  → blocking call

Are tasks unfinished?
  → forgot await or gather

Is system slow?
  → missing concurrency or semaphore too strict

Does shutdown hang?
  → missing cancel or sentinel
```

---

# 10) Common async bugs

---

## Bug 1 — blocking event loop

```python
time.sleep()
```

---

## Bug 2 — missing await

---

## Bug 3 — lost task

```python
asyncio.create_task(f())  # not awaited
```

---

## Bug 4 — no cancellation

---

## Bug 5 — mixing sync + async incorrectly

---

# 11) Practical patterns you now know

---

## Pattern A — Batch execution

→ `gather`

---

## Pattern B — Worker pipeline

→ `Queue`

---

## Pattern C — Rate-limited tasks

→ `Semaphore`

---

## Pattern D — Long-running service

→ cancellation

---

# 12) Interview storytelling

---

## Strong story 1

> I built an async API runner using `gather()` to execute many requests concurrently, reducing total runtime significantly compared to sequential execution.

---

## Strong story 2

> I implemented a queue-based async pipeline where producers generated tasks and workers processed them concurrently without shared-state locking.

---

## Strong story 3

> I used semaphores to enforce rate limits in an async system to prevent overwhelming an external API.

---

## Strong story 4

> I implemented graceful shutdown using cancellation to ensure long-running workers exited cleanly.

---

# 13) Interview questions

---

## Q — When would you use asyncio?

> When handling many I/O-bound tasks with async-compatible libraries.

---

## Q — Biggest async mistake?

> Blocking the event loop.

---

## Q — How do you limit concurrency?

> Using semaphores.

---

## Q — How do you handle shutdown?

> Using cancellation or sentinel values.

---

## Q — Async vs thread pool?

> Async is better for large-scale async I/O; thread pool is simpler for blocking tasks.

---

# 14) Final cheat sheet

```text
gather() → batch tasks
create_task() → start task
Queue → pipeline
Semaphore → limit concurrency
cancel() → stop task
wait_for() → timeout

Golden rule:
Never block event loop
```

---

# 15) Copy-ready notebook summary

```python
phase_4_summary = {
    "batch tasks": "use gather",
    "pipeline": "use Queue",
    "rate limit": "use Semaphore",
    "shutdown": "use cancel",
    "backpressure": "use bounded queue",
    "golden rule": "never block event loop"
}

for k, v in phase_4_summary.items():
    print(f"{k}: {v}")
```

---

# 16) Final recap

## You now know

* async foundations
* task management
* cancellation + timeouts
* queues + semaphores
* async vs threading vs multiprocessing
* real-world async design
* interview-level explanations

---

# 17) What you’ve achieved

You can now:

* **build async systems**
* **debug async bugs**
* **choose the right concurrency model**
* **explain async clearly in interviews**

---

# 18) Next best moves

1. Build 1 real project:

   * async crawler
   * async downloader
   * async job system

2. Practice:

   * explaining async vs threading
   * identifying bad async code

3. Optional next:

   * advanced asyncio (streams, networking)
   * system design with async

---

# 19) Final self-test

Answer confidently:

* Why is blocking the event loop dangerous?
* When should you use async instead of threading?
* How do you limit concurrency?
* How do you shut down async workers?
* What is the biggest async mistake?

---

Nice — this is the perfect moment to level up from “I understand async” → **“I can prove it in interviews + projects”** 🚀

We’ll do this in the most high-impact way:

---

# 🔥 Next Phase — Real Project + Mock Interview Training

## Mental model

1. **Build something real → confidence**
2. **Explain it clearly → interview success**
3. **Debug it → mastery**
4. **Compare approaches → senior thinking**

---

# 🧩 Part 1 — Resume-Level Async Project

## Project: **Async Web Crawler (with rate limiting + pipeline)**

---

## 🧠 Problem statement

Build a system that:

* takes a list of URLs
* fetches them concurrently
* limits concurrency (rate limit)
* processes results
* stores output
* shuts down cleanly

---

## 🏗️ Architecture

```text
URL list
   ↓
Producer
   ↓
Queue
   ↓
Workers (Semaphore limited)
   ↓
Result Queue
   ↓
Aggregator
```

---

## 🧱 Components

| Component         | Tool            |
| ----------------- | --------------- |
| Fetching          | async tasks     |
| Rate limiting     | `Semaphore`     |
| Task distribution | `Queue`         |
| Result collection | result queue    |
| Shutdown          | sentinel values |

---

## 💻 Full Project Code

```python
import asyncio
import random

# Queues
url_queue = asyncio.Queue()
result_queue = asyncio.Queue()

# Limit concurrent requests
sem = asyncio.Semaphore(3)

# Fake fetch
async def fetch(url):
    async with sem:
        print(f"Fetching {url}")
        await asyncio.sleep(random.uniform(1, 2))
        return f"data_from_{url}"

# Worker
async def worker(name):
    while True:
        url = await url_queue.get()
        if url is None:
            print(f"{name} exiting")
            break

        data = await fetch(url)
        await result_queue.put((url, data))
        url_queue.task_done()

# Producer
async def producer(urls):
    for url in urls:
        await url_queue.put(url)

    # send stop signals
    for _ in range(3):
        await url_queue.put(None)

# Aggregator
async def aggregator():
    results = []
    while True:
        try:
            item = await asyncio.wait_for(result_queue.get(), timeout=3)
            results.append(item)
        except asyncio.TimeoutError:
            break
    return results

# Main
async def main():
    urls = [f"url_{i}" for i in range(10)]

    workers = [asyncio.create_task(worker(f"W{i}")) for i in range(3)]

    await producer(urls)
    await url_queue.join()

    for w in workers:
        await w

    results = await aggregator()

    print("\nFinal Results:")
    for r in results:
        print(r)

await main()
```

---

## 🧠 What this project proves

You understand:

* async concurrency
* queues
* semaphores (rate limiting)
* worker pipelines
* graceful shutdown
* structured flow

---

## 💬 Interview story (VERY important)

Say this:

> I built an async web crawler where a producer enqueued URLs, worker tasks fetched them concurrently with a semaphore to enforce rate limits, and results were collected via a result queue. I used sentinel values for clean shutdown and avoided shared-state mutation by using queues.

That is a **strong, real-world answer**.

---

# 🧪 Part 2 — Debugging Drill (Critical Skill)

## Buggy Code

```python
import time

async def bad():
    time.sleep(2)
    print("done")

await asyncio.gather(bad(), bad())
```

---

## 🎯 What’s wrong?

### Answer

* `time.sleep()` blocks event loop
* tasks cannot run concurrently

---

## Fix

```python
await asyncio.sleep(2)
```

---

## Interview Answer

> This blocks the event loop. In asyncio, all blocking calls must be replaced with async equivalents or offloaded to executors.

---

# ⚔️ Part 3 — Decision Drill (Very High Value)

## Question

You have:

* 5000 API requests
* async HTTP library available

### What do you use?

✅ Asyncio

---

## Twist

* library is blocking

### Answer

✅ ThreadPoolExecutor or threads

---

## Twist 2

* CPU-heavy parsing

### Answer

✅ multiprocessing (or hybrid)

---

## Golden answer

> I choose based on bottleneck: async for I/O, threads for blocking I/O, multiprocessing for CPU-bound work.

---

# 🎤 Part 4 — Mock Interview (You answer)

Let’s simulate real interview pressure.

---

## Question 1

**Why is blocking the event loop dangerous?**

---

## Question 2

**When would you use asyncio instead of threading?**

---

## Question 3

**Design a system to process 10,000 URLs efficiently**

---

## Question 4

**What is the difference between `gather()` and `create_task()`?**

---

## Question 5

**How do you shut down async workers cleanly?**

---

👉 Reply with your answers — I’ll critique like an interviewer (this is where real improvement happens).

---

# 🧠 Part 5 — What you should do next

## Immediate actions

1. Run the project
2. Modify it:

   * add timeout
   * add retry
   * change worker count
3. Explain it out loud (VERY important)

---

## Optional upgrade (strong)

Turn this into:

* GitHub repo
* add README:

  * architecture diagram
  * explanation
  * tradeoffs

---

# 🏁 Final milestone

You are now at:

```text
Beginner → Intermediate → Practical → Interview-ready
```

---

# 🚀 If you want next level

I can:

* 🔥 grill you with **hard async interview questions**
* 🧠 give **system design concurrency problems**
* 🧩 build **advanced async (real HTTP, aiohttp, websockets)**
* 🧪 give **tricky bug scenarios**

---


# Async in FastAPI: the mental model first

## 1) The core idea

* **Async is best for waiting tasks**, not for heavy computation.
* It helps one thread do useful work while waiting for slow I/O like:

  * network calls
  * database queries
  * file access
  * external APIs

### Simple picture

```text
Sync / blocking:
Task 1 ----wait----done
Task 2 ----wait----done
Task 3 ----wait----done

Async / non-blocking:
Task 1 --wait--
Task 2 --wait--
Task 3 --wait--
         | while waiting, switch to another task |
```

---

## 2) What `asyncio` is

* `asyncio` is Python’s built-in library for **running async code**.
* It gives you:

  * an **event loop**
  * `async def`
  * `await`
  * tasks and concurrency without one thread per task

### Think of it like this

* The **event loop** is a manager.
* It gives each task a turn.
* When a task says `await`, it is saying:

```text
"I'm waiting. Let someone else run."
```

---

## 3) Why async exists

A lot of programs are not CPU-bound. They are **I/O-bound**.

### Example

A web API might:

* receive request
* call database
* call another API
* send response

Most of that time is spent **waiting**, not calculating.

Async helps you handle more requests efficiently because while one request is waiting, the server can work on another request.

---

## 4) A tiny async example

```python
import asyncio

async def fetch_data(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")
    return name

async def main():
    task1 = asyncio.create_task(fetch_data("A", 2))
    task2 = asyncio.create_task(fetch_data("B", 2))

    results = await asyncio.gather(task1, task2)
    print(results)

asyncio.run(main())
```

### What happens

* Without async, two 2-second waits could take about **4 seconds**
* With async, they can complete in about **2 seconds**

Why?

* while `A` is sleeping, `B` can run
* `sleep` here is non-blocking

---

## 5) Async vs multithreading

### The short truth

* **Async** is usually better for **many I/O tasks**
* **Multithreading** is often better when you must use blocking libraries or legacy code
* Neither is magic for CPU-heavy work

### Compare them

| Aspect            | Async                          | Multithreading                                         |
| ----------------- | ------------------------------ | ------------------------------------------------------ |
| Best for          | I/O-heavy work                 | Blocking code, legacy libs                             |
| Memory cost       | Low                            | Higher                                                 |
| Context switching | Managed by event loop          | Managed by OS threads                                  |
| Complexity        | Can be cleaner once understood | Can get tricky with locks/races                        |
| CPU-heavy work    | Not ideal                      | Also limited by GIL in Python for pure Python CPU work |

---

## 6) Why async over multithreading in FastAPI

FastAPI is built to work very well with async endpoints.

### Reason 1: Better scaling for I/O-heavy apps

If you have many requests waiting on DB/API calls, async lets one worker handle more concurrent waiting.

### Reason 2: Lower overhead

Threads cost memory and scheduling overhead. Async tasks are lighter.

### Reason 3: Cleaner concurrency model for web APIs

In web APIs, most work is waiting on external services. Async fits that pattern naturally.

---

## 7) Important Python reality: the GIL

* Python has the **GIL** for CPython.
* That means **threads do not give true parallelism for pure Python CPU work**.
* So for CPU-heavy tasks, threads are not the big win people expect.

### So:

* **I/O-bound** → async often wins
* **CPU-bound** → use multiprocessing, task queues, native extensions, or offload work

---

## 8) When to use async

Use async when your code mostly does **waiting**.

### Good fits

* calling web APIs
* database access with async drivers
* multiple network requests
* websocket servers
* many concurrent clients

### Not a good fit

* image processing
* large number crunching
* heavy compression
* complex CPU work in request handler

---

## 9) FastAPI example: sync vs async endpoint

### Async endpoint

```python
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(2)
    return {"message": "done async"}
```

### Sync endpoint

```python
from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/sync")
def sync_endpoint():
    time.sleep(2)
    return {"message": "done sync"}
```

### What is the difference?

* `asyncio.sleep(2)` **does not block the event loop**
* `time.sleep(2)` **blocks the thread**

In a real app, if one request blocks, the server cannot use that same execution path to help another waiting async task.

---

## 10) The most important rule

### Do not mix async code with blocking calls carelessly

Bad example:

```python
import time

async def bad():
    time.sleep(2)   # blocks everything
```

Better:

```python
import asyncio

async def good():
    await asyncio.sleep(2)
```

### In real FastAPI code

If you use async endpoints, also use:

* async database libraries
* async HTTP clients like `httpx.AsyncClient`
* non-blocking file/network operations where possible

---

## 11) A practical decision tree

```text
Is the task mostly waiting on I/O?
    yes -> async is a strong choice
    no  -> is it CPU heavy?
              yes -> use multiprocessing / background jobs
              no  -> normal sync code may be fine
```

---

## 12) How I would learn FastAPI efficiently

1. Learn **Python functions and decorators**
2. Learn **async / await**
3. Learn **event loop and I/O-bound vs CPU-bound**
4. Learn **FastAPI routing and request/response**
5. Learn **Pydantic models**
6. Learn **database access**
7. Learn **dependency injection**
8. Learn **background tasks and deployment**

---

## 13) My direct advice

* **Yes, asyncio is the right place to start** before FastAPI.
* If async feels confusing, that is normal. The key is this:

  * **async is not about doing more work**
  * it is about **not wasting time while waiting**

---

## 14) A very short memory hook

```text
Async = one worker switching between waiting jobs
Threads = more workers, more overhead
CPU-heavy = neither is the main answer
I/O-heavy = async shines
```

## Next useful topic order

* `async def` vs normal `def`
* `await` and `asyncio.gather`
* event loop explained with a real timeline
* how FastAPI runs sync vs async endpoints
* async database calls in FastAPI
* common mistakes with blocking code







