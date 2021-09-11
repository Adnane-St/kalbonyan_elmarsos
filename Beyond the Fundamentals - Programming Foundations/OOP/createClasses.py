class Pet:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.isAlive = True
    
    def talk(self):
        if self.isAlive:
            print("Name: {}.\ntype: {}.".format(self.name,self.type))
    def kill(self):
        self.isAlive = False

pet1 = Pet("Mimi","Cat")
pet1.talk()

pet2 = Pet("Bigy","Cat")
pet2.isAlive = False
pet2.talk()

