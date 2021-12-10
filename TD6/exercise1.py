import threading
import time

MAX_PHILOSOPHERS = 5
philosopherLoop = True

def philosopher(i, chopstick):
    while philosopherLoop:
        print("Starting thread:", threading.current_thread().name)
        print("I'm thinking", i)
        time.sleep(1)
        first_stick = i if i % 2 == 0 else (i+1) % MAX_PHILOSOPHERS
        second_stick = (i+1) % MAX_PHILOSOPHERS if i % 2 == 0 else i

        chopstick[first_stick].acquire()
        chopstick[second_stick].acquire()
        print ("I'm eating", i)
        time.sleep(1.5)
        chopstick[first_stick].release()
        chopstick[second_stick].release()

if __name__ == "__main__":
    print("Starting thread:", threading.current_thread().name)

    lock = []
    for i in range(MAX_PHILOSOPHERS):
        lock.append(threading.Lock())

    threads = [threading.Thread(target=philosopher, args=(i, lock)) for i in range(MAX_PHILOSOPHERS)]

    for thread in threads:
        thread.start()

    time.sleep(20)
    philosopherLoop = False

    for thread in threads:
        thread.join()

    print("Ending thread:", threading.current_thread().name) 
    
