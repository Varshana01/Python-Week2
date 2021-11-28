# What is a class?
#--A Class is like an object constructor, or a "blueprint" for creating objects.
# What is an instance?
#--It is  an individual object of a certain class.
# What is encapsulation?
#It describes the idea of wrapping data and the methods that work on data within one unit.
# What is abstraction?
#Abstraction is hiding the implementation and only showing the features we want.
# What is inheritance?
# Inheritance is the capability of one class to derive or inherit the properties from another class.
# What is multiple inheritance?
#Multiple Inheritance is a type of inheritance in which one class can inherit properties (attributes and methods) of more than one parent classes.
# What is polymorphism?
#polymorphism means the same function name (but different signatures) being used for different types.
# What is method resolution order or MRO?
#It denotes the way a programming language resolves a method or attribute.

import itertools, random

class Card:

    deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
    random.shuffle(deck)

    print("You got:")
    for i in range(1):
        print(deck[i][0], "of", deck[i][1])

deck = Card()