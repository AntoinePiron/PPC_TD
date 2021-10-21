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
    p = Fibonnacci(int(sys.argv[1]))
    p.start()
    p.join()