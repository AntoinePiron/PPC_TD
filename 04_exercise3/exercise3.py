from multiprocessing import Process, Pipe
import string

class Child(Process):
    def __init__(self, connection):
        super().__init__()
        self.connection = connection
    def run(self):
        phrase = self.connection.recv()
        split = phrase.split()
        endstrng = ""
        for i in range(len(split)):
            endstrng += split[(len(split)-1)- i] + " "
        self.connection.send(endstrng)
        self.connection.close()


if __name__ == "__main__":
    parent_connection, child_connection = Pipe()
    p = Child(child_connection)
    p.start()
    send = input("Write a phrase : ")
    parent_connection.send(send)
    print(parent_connection.recv())
    parent_connection.close()
    p.join()