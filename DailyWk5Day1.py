class Farm:
    def __init__(self, name):
        self.name = name
        self.animals={}


    def add_animal(self, animal_name, amount=1):
        if animal_name in self.animals:
            self.animals[animal_name] += amount

        else:
            self.animals[animal_name] = amount


    def get_info(self):
        pass

macdonald=Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.animals)
print("E I E I O")






























# #______________________________________________________
# def deposit(self, amount):
#         if amount <= 0:
#             print("Invalid amount")
#         elif amount < 100:
#             print("Minimum deposit is 100")
#         else:
#             self.balance += amount
#             self.transactions.append(f"Deposit: {amount}")
#             print("Deposit Succcessful")