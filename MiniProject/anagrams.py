from anagram_checker import AnagramChecker
from itertools import permutations

class word_anagram(AnagramChecker):
    word = input("Enter a word or press Q to quit: ")
    active = True
    while active:
        if word == "Q":
            active = False
        else:
            active = False
    if " " in word:
        word.strip()
    anagram_word=[''.join(element) for element in list(permutations(word))]
    print(f"YOUR WORD : {word} \n this is a valid English word \n Anagram for you word: {anagram_word}")

Anagram= word_anagram()