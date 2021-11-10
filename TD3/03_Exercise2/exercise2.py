import sys
import threading
from queue import Queue
from statistics import mean, median, stdev

def worker(in_queue, out_queue, data_ready, data):
    data_ready.wait()
    for func in list(in_queue.queue):
        out_queue.put((func.__name__, func(data)))

if __name__ == "__main__":

    in_queue = Queue()
    out_queue = Queue()
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
    thread = threading.Thread(target=worker, args=(in_queue, out_queue,data_ready, data))
    thread.start()
    ops = [min, max, mean, median, stdev]
    for op in ops:
        in_queue.put(op)
    data_ready.set()
    thread.join()

    for tup in list(out_queue.queue):
        name, value = tup
        print(name, ":", value)
