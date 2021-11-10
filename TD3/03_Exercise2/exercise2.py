import threading
from queue import Queue

def worker(queue, data_ready):
    pass

if __name__ == "__main__":
    queue = Queue()
    data_ready = threading.Event()

    thread = threading.Thread(target=worker, args=(queue,data_ready))
    thread.start()