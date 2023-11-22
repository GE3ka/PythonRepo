
class Pet:
    def __init__(self,name,type,tricks):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=100
        self.energy=100
    def sleep(self):
        self.energy+=25
        return self
    def eat(self):
        self.energy+=5
        self.health+=10
        return self
    def play(self):
        self.health+=5
        return self
    def noise(self):
        if self.type =="Dog":
            print(f" haw haw haw ! ") 
        if self.type=="Cat":
            print(f"miaou miaou miaou ! ") 

class Bird(Pet):
    def __init__(self, name, type, tricks,age):
        super().__init__(name, type, tricks)
        self.age=age
    def play(self):
        print ("I'm a bird so I wont be walking but I would like to play bird games ...")   
    def noise(self):
        if self.type=="bird":
            print(f"Ziw Ziw Ziw")    