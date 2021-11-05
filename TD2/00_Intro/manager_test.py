from multiprocessing import Process, Manager

def f(d,l):
    d[1] = 'one'
    d['two'] = 2
    l.reverse()

if __name__ == "__main__":
    with Manager() as manager:
        dct = manager.dict()
        lst = manager.list(range(10))

        p = Process(target=f, args=(dct,lst))
        p.start()
        p.join()

        print(dct)
        print(lst)