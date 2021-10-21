from multiprocessing import Process, process

#Deuxième méthode en définissant une clase
class Greet(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print("Hello, ", self.name, " !")

#Première technique en définisssant une méthode
def greet(name):
    print("Hello, ", name, "!")

if __name__ == "__main__":
    #Première méthode
    p = Process(target=greet, args=("Kitty",))
    p.start()
    p.join()

    #Deuxièmre méthode 
    p2 = Greet("Kitty")
    p2.start()
    p2.join()