from classes.ninja import Ninja
from classes.pirate import Pirate
import random

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")
user_answer=""


while michelangelo.health>0 and jack_sparrow.health>0:
    adversaire=random.randint(1,2)
    user_answer=input("please enter \n 1: Attack \n 2: Defence")
    if user_answer=="1":
        if adversaire==1:
            jack_sparrow.attack(michelangelo)
            michelangelo.attack(jack_sparrow)
            print("The pirate is attacking!")
        if adversaire==2:
            michelangelo.attack(jack_sparrow)
            jack_sparrow.defence()   
            print("The pirate is defending him self !!") 
    if user_answer=="2":
        if adversaire==1:
            jack_sparrow.defence()
            michelangelo.attack(jack_sparrow)
            print("The pirate is attacking!")
        if adversaire==2:
            michelangelo.defence(jack_sparrow)
            jack_sparrow.defence()  
            print("The pirate is defending him self !!") 
    else:
        print ("wrong choice , you were hit") 
        jack_sparrow.attack(michelangelo)
        print("The pirate is attacking!")
    jack_sparrow.show_stats()
    michelangelo.show_stats()    

