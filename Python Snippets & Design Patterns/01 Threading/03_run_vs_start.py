import threading
import time

def worker():
    print(f"Running in {threading.current_thread().name}")
    time.sleep(1)
    print("worker done")

print("Main thread name:", threading.current_thread().name)

t = threading.Thread(target=worker, name="MyWorker")

print("\nCalling run() directly:")
t.run()

print("\nCalling start():")
t2 = threading.Thread(target=worker, name="MyRealThread")
t2.start()
t2.join()

print("\nMain finished")