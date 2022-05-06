from random import randint
from bunnyFuncs import random_name

class bunny():
    #Attributes

    #Contructors
    def __init__(self,sex,colour,name,bunny_rmvb,bunny_tvs): #rmvb stands for Radioactive Mutant Vampire Bunny, tvs stands for The Vampire Slayer
        self.is_rmvb = bunny_rmvb
        self.is_tvs = bunny_tvs
        self.sex = sex
        self.colour = colour
        self.age = 0
        self.name = name
        self.is_alive = True

    #Methods

    def grow_older(self):
        self.age = self.age + 1 

    def die(self):
        self.is_alive = False

    def give_birth(self):
        new_sex_int = randint(0,1)
        if new_sex_int == 0:
            sex = "male"
        else:
            sex = "female"
        colour = self.colour
        name = random_name()
        random_number = randint(1,100)
        if random_number == 1 or random_number == 2:
            rmvb = True
        else:
            rmvb = False
        tvs = False  
        new_bunny = bunny(sex,colour,name,rmvb,tvs)
        return new_bunny

    def turn_evil(self):
        self.is_rmvb = True