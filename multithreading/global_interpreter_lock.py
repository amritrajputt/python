import threading
import time

def brew_coffee(name):
    print(f"Brewing {threading.current_thread().name} started...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Brewing {threading.current_thread().name} finished...")

thread1 = threading.Thread(target=brew_coffee, name="Coffee-1")
thread2 = threading.Thread(target=brew_coffee, name="Coffee-2")
start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
end = time.time()
print(f"Time taken: {end-start}")