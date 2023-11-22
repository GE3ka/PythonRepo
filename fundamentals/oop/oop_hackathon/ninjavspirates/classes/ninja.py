class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.shield=100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n Shield: {self.shield}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        if pirate.health<0:
            pirate.health=0
        return self
    def defence(self,pirate):
        if self.shield >0 and self.health>0:
            self.shield -=10
        else:
            print(f"The pirate won, Game over") 
