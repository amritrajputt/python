import threading 
import time
import random

def task1(name):
    print("amrit")
    time.sleep(random.randint(1,5))
    print(f"{name} completed task1")

threads = []

for i in range(10):
    t = threading.Thread(target=task1,args =(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads have completed their tasks.")
