import threading
import time

def fake_io_task(name, delay):
    print(f"{name}: starting request")
    time.sleep(delay)
    print(f"{name}: response received")

start = time.time()

threads = [
    threading.Thread(target=fake_io_task, args=("Task1", 2)),
    threading.Thread(target=fake_io_task, args=("Task2", 2)),
    threading.Thread(target=fake_io_task, args=("Task3", 2)),
    threading.Thread(target=fake_io_task, args=("Task4", 2)),
    threading.Thread(target=fake_io_task, args=("Task5", 2))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time.time()

print(f"Total time: {end - start:.2f} seconds")
