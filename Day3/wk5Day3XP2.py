
# ExecisesXP2
#Exercise 1
import datetime
# today = datetime.date.today()
# def toDay():
#     print ("today is:",today)
#
# toDay()
#
# #Exercise 2
# from datetime import datetime
# def now_jan():
#     jan = datetime(2022, 1, 1)
#     diff = jan-datetime.now()
#     print(f'The 1st of January is in {abs(diff)} hours')
# now_jan()
#
# #Exercise 3
# def min_alive(birthdate):
#
#     date = datetime.strptime(birthdate, '%d/%m/%Y')
#     print(date)
#     age = int(((datetime.today() - date).days/365))
#     minutes = age * 525600
#     print(f'you have been alive for {minutes} minutes')
#
# # min_alive("12/07/2000")
# #Exercise 4
# from datetime import datetime
# def next_holiday():
#     christmas = "25/12/2021"
#     dt = datetime.strptime(christmas, "%d/%m/%Y")
#     time = int((dt - datetime.today()).days)
#     return f"Today is the {datetime.today().day},Christmas is in {time} days."
# print(next_holiday())
# #Exercise 5 : How Old Are You On Jupiter?
# class Planet:
#     def calculate_age(self, age, planet):
#         # Convert age in seconds to years
#         age = age / 1000000000 * 31.69
#         age_value = 1
#         if planet == "Mercury":
#             age_value = 0.2408467
#         elif planet == "Venus":
#             age_value = 0.61519726
#         elif planet == "Mars":
#             age_value = 1.8808158
#         elif planet == "Jupiter":
#             age_value = 11.862615
#         elif planet == "Saturn":
#             age_value = 29.447498
#         elif planet == "Uranus":
#             age_value = 84.016846
#         elif planet == "Neptune":
#             age_value = 164.79132
#         else:
#             raise Exception("Error: Please enter a valid planet")
#         new_age = age / age_value
#         print(f"Your age on {planet} is: {new_age} years old")
#         # return new_age
# year = Planet()
# year.calculate_age(20, "Mercury")
# year.calculate_age(1000000000, "Neptune")
# #year.calculate_age(1000000000, "Pluto")
##############or##########
# earth_year_in_secs = float(input("How old are you in seconds? "))
# planets = {
#     "Earth":  (earth_year_in_secs * 1 / 60 /60 / 24 / 365),
#     "Mercury": (earth_year_in_secs * 0.2408467) / 60/ 60/ 24 / 365,
#     "Venus": (earth_year_in_secs * 0.61519726) / 60/ 60/ 24 / 365,
#     "Mars": (earth_year_in_secs * 1.8808158) / 60/ 60/ 24 / 365,
#     "Jupiter": (earth_year_in_secs * 11.862615) / 60/ 60/ 24 / 365,
#     "Saturn": (earth_year_in_secs * 29.447498) / 60/ 60/ 24 / 365,
#     "Uranus": (earth_year_in_secs * 84.016846) / 60/ 60/ 24 / 365,
#     "Neptune": (earth_year_in_secs * 164.79132) / 60/ 60/ 24 / 365
# }
# planets = planets.items()
# for planet, time in planets:
#    print("The planet is", planet, "and you are", time, "earth-years old.")
#Exercise 6 : Faker Module
# from faker import Faker
# import random
# fake = Faker()
# fake_names = []
# fake_addresses = []
# for i in range(10):
#     fake_names.append(fake.name())
#     fake_addresses.append(fake.address())
# users = []
# def new_users(**kwargs):
#     users.append(kwargs)
#     return users
# new_users(name=random.choice(fake_names),
#           address=random.choice(fake_addresses))
# new_users(name=random.choice(fake_names),
#           address=random.choice(fake_addresses))
# print(new_users())