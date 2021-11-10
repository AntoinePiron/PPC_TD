import sys
import threading
from queue import Queue
from statistics import mean, median, stdev

def worker(queue, data_ready, data):
    data_ready.wait()
    for elem in list(queue.queue):
        func = queue.get()
        print(func.__name__, " : ", func(data))

if __name__ == "__main__":

    queue = Queue()
    data_ready = threading.Event()

    data = []
    #ctrl d pour arreter d'ecrire
    input_str = sys.stdin.read().split()
    print(input_str)
    for s in input_str:
        try:
            x = float(s)
        except ValueError:
            print("bad number", s)
        else:
            data.append(x)
    thread = threading.Thread(target=worker, args=(queue,data_ready, data))
    thread.start()
    ops = [min, max, mean, median, stdev]
    for op in ops:
        queue.put(op)
    data_ready.set()

    thread.join()
