import threading
import time
cache = {}
lock = threading.Lock()
def get_data(key):
    if key in cache:
        print(f"{threading.current_thread().name} fetched from cache")
        return cache[key]
    with lock:
        if key in cache:
            print(f"{threading.current_thread().name} fetched from cache")
            return cache[key]
        print(f"{threading.current_thread().name} computing result for key: {key}")
        time.sleep(2)
        value = f"Data_for_{key}"
        cache[key] = value
        return value
def worker(key):
    result = get_data(key)
    print(f"{threading.current_thread().name} received: {result}")
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=("User1234",), name=f" Thread-{i+1}")
    threads.append(t)
    t.start()
for t in threads:
    t.join()



# OUTPUT:
# Thread-1 computing result for key: User1234
# Thread-1 received: Data_for_User1234
# Thread-2 fetched from cache
# Thread-2 received: Data_for_User1234
# Thread-3 fetched from cache
# Thread-3 received: Data_for_User1234
