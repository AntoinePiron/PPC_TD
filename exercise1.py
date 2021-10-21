from multiprocessing import Process

class Fibonnacci(Process):
    def __init__(self, num):
        super().__init__()
        self.num = num
    def run(self):
        #On initialise les valeurs de base
        fnm2 = 0
        fnm1 = 1
        fiblis = [fnm2, fnm1]
        for _ in range(self.num-1):
            fn = fnm1 + fnm2
            fiblis.append(fn)
            fnm1, fnm2 = fn, fnm1
        print(fiblis)
        

if __name__ == "__main__":
    p = Fibonnacci(5)
    p.start()
    p.join()