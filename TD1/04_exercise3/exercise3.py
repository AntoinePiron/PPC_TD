from multiprocessing import Process, Pipe

#Notre class qui va nous servir pour le processus 
class Child(Process):

    def __init__(self, connection):
        super().__init__()
        self.connection = connection
        
    def run(self):
        #On créé ici aussi une boucle infinie
        while True:
            #On récupere dans un premier temps la phrase
            phrase = self.connection.recv()
            if phrase == "end":
                self.connection.close()
                return
            #On la split pour inverser les mots
            split = phrase.split()
            endstrng = ""
            #On parcours le tableau pour inverser les mots
            for i in range(len(split)):
                endstrng += split[(len(split)-1)- i] + " "
            #On les envoies sur le pipe 
            self.connection.send(endstrng)
            #On oublie pas de refermer la connection


if __name__ == "__main__":
    #création du pipe
    parent_connection, child_connection = Pipe()
    #Instantiation de notre child
    p = Child(child_connection)
    #demarrage du process
    p.start()
    #On créé une boucle infini afin de permettre plusieurs envoie
    while True:
        #On récupere la phrase en input puis on l'envoie
        send = input("Write a phrase : ")
        parent_connection.send(send)
        if send == "end":
            print("End of communication...")
            break
        #On récupere alors la reponse
        print(parent_connection.recv())
    parent_connection.close()
    p.join()