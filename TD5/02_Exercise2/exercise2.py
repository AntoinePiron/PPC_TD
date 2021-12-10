from multiprocessing import Process, Lock, Semaphore
import sys
       
def producer(num,fiblis):
    for i in range(2,num+1):
            fiblis.append(fiblis[i-1] + fiblis[i -2])

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
    
    mutex = Lock()
    full = Semaphore(0)
    