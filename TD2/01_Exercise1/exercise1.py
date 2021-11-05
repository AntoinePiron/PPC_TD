from multiprocessing import Process, Manager
import sys

class Fibonnacci(Process):
    def __init__(self, num, fiblis):
        super().__init__()
        self.num = num
        self.fiblis = fiblis

    def run(self):
        for i in range(2,self.num+1):
            self.fiblis.append(self.fiblis[i-1] + self.fiblis[i -2])
        

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
    
    with Manager() as manager:
        #On génère notre shared data
        fiblis = manager.list([0,1])
        #Si on se retoruve ici c'est qu'aucune exception n'a été soulevé donc on peut lanceer notre process
        p = Fibonnacci(argument, fiblis)
        p.start()
        p.join()
        #Si tous se passe bien on print une liste modifié
        print(fiblis)
