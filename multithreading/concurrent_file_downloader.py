import threading
import time

def download_file(file_name):
    print(f"Downloading {file_name}")
    time.sleep(5)
    print(f"Downloaded {file_name}")

threads = []

if __name__ == "__main__":
    for i in range(11):
        t = threading.Thread(target=download_file, args=(f"file-{i+1}.txt",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads have completed their tasks.")