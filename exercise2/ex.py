import os
import signal
from multiprocessing import Process
import time

#On va créer le process child avec une classe
class Child(Process):
    def __init__(self):
        super().__init__()
    def run(self):
        time.sleep(5)
        #On envoie le sigint avec le PID du parent 
        os.kill(os.getppid(), signal.SIGINT)
        #On le fait rentrer dans un boucle infini pour bien vérifier que c'est le parent qui le kill
        while True:
            pass

def handler(sig, frame):
    if sig == signal.SIGINT:
        #On fait un print de debug
        print("It works")
        #Puis on kill le process
        os.kill(p.pid, signal.SIGKILL)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)
    p = Child()
    p.start()
    p.join()