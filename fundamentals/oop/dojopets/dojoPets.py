import pets
class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet
    def walk(self):
        self.pet.play()
    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.noise()                  


first_pet=pets.Pet("Fox","Dog","Catch the Ball")
owner_first_pet=Ninja("José","Georges","good","Flea and tick",first_pet)
owner_first_pet.bathe()
owner_first_pet.walk()
owner_first_pet.feed()
second_pet=pets.Bird("Malih","Bird","Hide and seek","3 months")
owner_second_pet=Ninja("Marta","Bellie","great","birds food",second_pet)
owner_second_pet.bathe()
owner_second_pet.walk()
owner_second_pet.feed()
