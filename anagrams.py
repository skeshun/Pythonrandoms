# Check if two words are anagrams 
# Example:
from itertools import permutations,combinations
import enchant

word = input("Raw word :")
anagram = input("Anagram word :")
dictionary = enchant.Dict("en_US")
letters = [chr for chr in word]
repeatedword = []

def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    if (sorted(word) == sorted(anagram)):
        return True
    else:
        return False
            



def solve_anagram(word,dictionary,letters,repeatedword):
    for number in range(3,len(letters)+1): #For Loop
        for current_set in combinations(letters,number): #Combinations Function
            #Code for the Basic Anagram Finder
            for current in permutations(current_set):
                current_word = ''.join(current)
                if dictionary.check(current_word)and current_word not in repeatedword:
                    print(current_word)
                    repeatedword.append(current_word)
                    return ("complete")

print("Anagram found is :",find_anagram(word, anagram))
print("Anagram is ",solve_anagram(word,dictionary,letters,repeatedword))