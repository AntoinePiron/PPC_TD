from multiprocessing import Process
import sys
import time
import os

class Fibonnacci(Process):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        print("Process PID", os.getpid())
        print("Parent process PID", os.getppid())
        fiblis = [0, 1]
        for i in range(2,self.num+1):
            fiblis.append(fiblis[i-1] + fiblis[i -2])
        print(fiblis)
        time.sleep(5)
        

if __name__ == "__main__":
    #On vient tester si on peut convertir en int et la positivité
    try:
        argument = int(sys.argv[1])
        if argument < 0 :
            raise ValueError
    except:
        #Si jamais on a relevé une exception on exit simplement le programme
        print("Argument invalide")
        exit(1)
    
    #Si on se retoruve ici c'est qu'aucune exception n'a été soulevé donc on peut lanceer notre process
    p = Fibonnacci(argument)
    p.start()
    p.join()
