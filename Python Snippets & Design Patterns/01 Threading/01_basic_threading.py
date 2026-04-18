import threading
import time

def worker(name, delay, repeat):
    for i in range(repeat):
        print(f"{name} -> step {i+1}")
        time.sleep(delay)

t1 = threading.Thread(target=worker, args=("A", 0.5, 3))
t2 = threading.Thread(target=worker, args=("B", 0.3, 3))

t1.start()
t2.start()

t1.join()
t2.join()

print("Main thread: all workers finished")