from multiprocessing import Process
import sys

class Fibonnacci(Process):
    def __init__(self, num):
        super().__init__()
        self.num = num
    def run(self):
        fiblis = [0, 1]
        for i in range(2,self.num+1):
            fiblis.append(fiblis[i-1] + fiblis[i -2])
        print(fiblis)
        

if __name__ == "__main__":
    try:
        argument = int(sys.argv[1])
        if argument < 0 :
            raise ValueError
    except:
        print("Argument invalide")
        exit(1)

    p = Fibonnacci(argument)
    p.start()
    p.join()