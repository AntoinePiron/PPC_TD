import math
import multiprocessing
import random
import time

def is_prime(n):
    if n<2:
        return(n,False)
    if n == 2:
        return(n,True)
    if n%2 == 0:
        return(n,False)
    
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3,sqrt_n+1, 2):
        if n%i == 0:
            return(n,False)
    return(n,True)

if __name__ == "__main__":
    indexes = [random.randint(10**3,10**6) for i in range(10)]
    with multiprocessing.Pool(processes=2) as pool:

        start = time.time()
        print("*** Synchronous map")
        for x in pool.map(is_prime, indexes):
            print(x)
        end = time.time()
        timeElapsed = end-start
        print("Execution time:", timeElapsed)

        start = time.time()
        print("*** Asynchronous map")
        for x in pool.map_async(is_prime, indexes).get():
            print(x)
        end = time.time()
        timeElapsed = end-start
        print("Execution time:", timeElapsed)
        