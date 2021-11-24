# #Ex XP1
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Ragdoll(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# my_cats=[Bengal("Yasaar", 2), Chartreux('Oceanne', 6), Ragdoll('Varsh',5)]
#
# my_pets = Pets(my_cats)
# my_pets.walk()

# #Ex XP2
class Dog:
    def __init__(self,name,age,weight):
        self.name=name
        self.age = int(age)
        self.weight= int(weight)
    def bark(self):
        print(f"{self.name} is barking")
    def run_speed(self):
        return self.weight/self.age*10
    def fight(self, other_dog):
        self.other_dog=other_dog
        if int(self.run_speed()) * int(self.weight) > int(other_dog.run_speed()) * int(other_dog.weight):
            print(f"{self.name} won")
        else:
            print(f"{other_dog.name} has won")
#
# mi_pero1 = Dog("Rex", 3,10)
# mi_pero2 = Dog("Juan",2,12)
# mi_pero3 = Dog("waffy", 1,9)
# mi_pero1.fight(mi_pero2)

#Ex1 XP+
class Family():
    def __init__(self, last_name, members):
        self.members = members
        self.last_name = last_name
    def born(self, **new_member_info):
        new_member_info['age'] = 0
        new_member_info['is_child'] = True
        self.members.append(new_member_info)
        print("Congratulations on the new baby!")
    def is_18(self, member_name):
        for person in self.members:
            if person['name'] == member_name:
                return person['age'] >= 18
    def __repr__(self):
        family_members = 'The members of the family are:'
        for member in self.members:
            family_members += f'\t{member["name"]}'
        return family_members
smith = Family('Smith', [{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False}, {
                  'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}])
smith.born(name='Maya', gender='Female')
print(smith.is_18('Michael'))
print(smith)

#Ex2 XP+

class TheIncredibles(Family):
    def use_power(self, name):
        for person in self.members:
            if person['name'] == name:
                if person['age'] >= 18:
                    print(person['power'])
                else:
                    raise Exception('You have no power here!')
    def incredible_presentation(self):
        for person in self.members:
            print(f"{person['name']}, your incredible name is {person['incredible_name']} and your incredible power is {person['power']}.")
    """The Parr family: Elastigirl(Helen), Mr. Incredible(Bob), Violet, and Dash. """
incredibles = TheIncredibles('Parr', [
    {'name': 'Bob', 'age': 40, 'gender': 'Male', 'is_child': False,
        'power': 'super strength', 'incredible_name': 'Mr. Incredible'},
    {'name': 'Helen', 'age': 36, 'gender': 'Female', 'is_child': False,
        'power': 'mutating body', 'incredible_name': 'Elastigirl'},
    {'name': 'Violet', 'age': 15, 'gender': 'Female', 'is_child': True,
        'power': 'invisibility and force fields', 'incredible_name': 'Invisigirl'},
    {'name': 'Dash', 'age': 10, 'gender': 'Male', 'is_child': True,
        'power': 'super speed', 'incredible_name': 'Speedy'}
])
incredibles.incredible_presentation()
incredibles.born(name='Baby Jack', gender='Male',
                 power='Unknown Power', incredible_name='SuperJack')
print(incredibles)
incredibles.incredible_presentation()