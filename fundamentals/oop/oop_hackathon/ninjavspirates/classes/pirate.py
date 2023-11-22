class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.shield=100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nShield: {self.shield}\n")

    def attack ( self , ninja ):
        
        ninja.health -= self.strength
        if ninja.health<0:
            ninja.health=0
        return self
    def defence(self):
        if self.shield >0 and self.health>0:
            self.shield -=10
        else:
            print(f"The Ninja won, Game over") 
        
