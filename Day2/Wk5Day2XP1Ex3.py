from Wk5Day2ExXP import Dog

class PetDog(Dog):
    def __init__(self, trained= False):
        self.trained = trained

    def train(self):
        print(Dog.bark())
        self.trained= True

    def play(self, *args):
        print(f"{args} all play together")
    play(Dog.__init__())

    def do_a_trick(self):
        if self.trained == True:
            print(f"{Dog.__init__()} do this")
        else:
            pass

my_dog = PetDog()
