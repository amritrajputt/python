from multiprocessing import Process
import time

def task1(name):
    print(f" start {name}")
    time.sleep(3)
    print(f"{name} completed task2")

processes = []
if __name__ == "__main__":
    ...
for i in range(10):
    p = Process(target=task1,args =(f"Process-{i}",))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print("All processes have completed their tasks.")