from multiprocessing import Process, Value, Array

#Notre fonction qui sera lancée comme un process
def f(n,a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == "__main__":
    #ici le d permet d'indiquer un double precision float
    number = Value('d', 0.0)
    #Le i correspond donc à integer ici
    vector = Array('i', range(10))

    p = Process(target=f, args=(number, vector))
    p.start()
    p.join()

    print(number.value)
    print(vector[:])