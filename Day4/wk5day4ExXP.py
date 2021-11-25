# Exercise 1
import random
def get_words_from_file(file):
    with open(file, 'r') as f:
        sentence = f.readlines()
        return sentence
def get_random_sentence(length):
    word_li = get_words_from_file("Random_Text.txt")
    li = []
    for _ in range(length):
        x = random.choice(word_li)
        li.append(x[:-2])
    return " ".join(li).lower()
def main():
    """this program will accept integer values between 2 and 20"""
    try:
        number_words = int(input('How long do you want the sentecne to be? enter an int between 2 and 20: '))
        if 2 <= number_words <= 20:
            return get_random_sentence(number_words)
        else:
            return 'your num is not between 2 and 20'
    except ValueError:
       return 'not a number'
print(main.__doc__)
print(main())

# # Exercise 2
#
# import json
# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payable":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
#
# sample_dict = json.loads(sampleJson)
# print(sample_dict["company"]["employee"]["payable"]["salary"])
# sample_dict["company"]["employee"]['birth_date'] = 2000/11/11
# print(sample_dict["company"]["employee"])
#
# sample_file = "filexp.json"
# with open('sample_json','w') as f:
#     json.dump(sample_dict,f,indent=4)
