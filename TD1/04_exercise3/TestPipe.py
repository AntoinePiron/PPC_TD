from multiprocessing import Process, Pipe

class Test(Process):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
    def run(self):
        self.connection.send([42, None, "Hello"])
        self.connection.close()


if __name__ == "__main__":
    #On génère notre pipe
    parent_conn, child_conn = Pipe()
    #On créé alors le process child en lui renseignant sa connection au pipe
    p = Test(child_conn)
    p.start()
    #Avec la méthode recv on recoit ceux qui provient du pipe
    print(parent_conn.recv())
    p.join()