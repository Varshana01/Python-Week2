# #XP exercise 1
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.felines = {}
#     def cats(self,cat_name, cat_age):
#         self.felines[cat_name]=cat_age
#
#
#
# list_cat = Cat("Feline",1)
# list_cat.cats('meow',4)
# list_cat.cats('brown',5)
# list_cat.cats('mink',3)
# print(list_cat.felines)
# print(dict(sorted(list_cat.felines.items(), key=lambda item: item[1])))
# keys = list(list_cat.felines.keys())
# list_cat.felines[list(list_cat.felines.keys()[-1])]

# #XP exercise 2
# class Dog:
#     def __init__(self,name,height):
#         self.name = name
#         self.height = int(height)
#
#     def bark(self):
#         print(f"{self.name} goes woof!")
#
#     def jump(self):
#         print(f"{self.name} jumps {self.height*2} cm high!")
#
# sarahs_dog = Dog("Teacup", 45)
# sarahs_dog.bark()
# sarahs_dog.jump()
# davids_dog = Dog("Teacup", 50)
# davids_dog.jump()
#
#
# bigger_dog = sarahs_dog.name
# if sarahs_dog.height > davids_dog.height:
#     print(bigger_dog)
#
# else:
#   print(davids_dog.name)
# #XP exercise 3
#
# class Song():
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print (line)
#
# stairway = Song(["There’s a lady who's sure",
#                      "all that glitters is gold",
#                      "and she’s buying a stairway to heaven"])
#
# print(stairway.sing_me_a_song())

 #XP exercise 4
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} already exists")
    def get_animals(self):
        print(self.animals)
        for animal in self.animals:
            print(animal)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} not in the zoo")
    def sort_animals(self):
        self.animals.sort()
        print(self.animals)
        self.animals = [list(filter(lambda animal: animal[0] == l, self.animals)) for l in sorted(list(set([animal[0] for animal in self.animals])))]
    def get_groups(self):
        for animal in self.animals:
            print(animal)
ramat_gan_safari = Zoo('Ramat Gan Safari')
ramat_gan_safari.add_animal('Ape')
ramat_gan_safari.add_animal('Anaconda')
ramat_gan_safari.add_animal('Buffalo')
ramat_gan_safari.add_animal('bear')
ramat_gan_safari.add_animal('crocodile')
ramat_gan_safari.add_animal('cougar')
ramat_gan_safari.add_animal('deer')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Ape')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()