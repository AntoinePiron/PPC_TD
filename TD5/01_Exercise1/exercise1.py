import sys
import multiprocessing
from multiprocessing import Process
from random import random

p_in = multiprocessing.Value('i', 0)

def generatePoints(n):
    print("Processse started")
    global p_in
    for _ in range(n):
        x, y = random()*2 - 1, random()*2 - 1
        if (pow(x, 2) + pow(y, 2)) <= 1:
            with p_in.get_lock():
                p_in.value += 1

if __name__ == "__main__":
    #On vérifie les différents erreurs possible du à l'entée utilisateur 
    if len(sys.argv) < 3:
        print("Please provide 2 arguments : number of points ans number of threads")
        sys.exit(1)
    
    try:
        numberOfPoints = int(sys.argv[1])
        numberOfProcesses = int(sys.argv[2])
    except ValueError:
        print("Value error in args")
        sys.exit(1)

    if numberOfPoints < 0 :
        print("Number of points need to be positive")
        sys.exit(1)

    with multiprocessing.Pool(processes=numberOfProcesses) as pool:
        for i in range(numberOfProcesses):
            pool.apply_async(generatePoints, (numberOfPoints,))

    app_pi = 4*(p_in.value/numberOfPoints*numberOfProcesses)
    print("Approximation of PI:", app_pi)