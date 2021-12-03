import sys
import threading
from random import random

def generatePoints(n):
    global p_in
    for _ in range(n):
        x, y = random()*2 - 1, random()*2 - 1
        if (pow(x, 2) + pow(y, 2)) <= 1:
            p_in += 1



if __name__ == "__main__":
    #On vérifie les différents erreurs possible du à l'entée utilisateur 
    if len(sys.argv) < 2:
        print("No arguments")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Wrong value")
        sys.exit(1)

    if n < 0 :
        print("Number of points need to be positive")
        sys.exit(1)
    
    p_in = 0

    thread = threading.Thread(target=generatePoints, args=(n,))
    thread.start()
    thread.join()

    app_pi = 4*(p_in/n)
    print("Approximation of PI:", app_pi)

