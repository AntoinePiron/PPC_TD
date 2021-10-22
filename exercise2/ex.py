import os
import signal
from multiprocessing import Process
import time

class Child(Process):
    def __init__(self):
        super().__init__()
    def run(self):
        time.sleep(5)
        os.kill(os.getppid, signal.SIGINT)

def handler(sig, frame):
    if sig == signal.SIGINT:
        print("Ca fonctionne")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    p = Child()
    p.start()
    p.join()