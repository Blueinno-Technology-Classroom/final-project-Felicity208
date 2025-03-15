import requests
from random import *



def check_def(word):
    if word != "checkdef":
        dict_response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()
        if "No Definitions Found" and "title" in dict_response:
            print(f"That's not a valid word! Enter a new word beginning with {computer[-1]}")
            return False
        else:
            return dict_response
    else:
        dict_def = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{computer}").json()
        return dict_def[0]


computer = requests.get('https://random-word-api.vercel.app/api').json()[0]

print(
    f"The first word is {computer}, now type a word starting with {computer[-1]}, or type 'checkdef' for the definition of the word")


while 1:
    player = input("Enter your word: ")

    if player == "checkdef":
        for words in check_def(computer):
            for meanings in words['meanings']:
                print(f"Parts of Speech:{meanings['partOfSpeech']}")
                for defs in meanings["definitions"]:
                    print(defs)

        print(f"Now type a word beginning with {computer[-1]}")

    else:
        player = player.lower()
        if player == "":
            print("Enter a valid word")

        if player[0] != computer[-1]:
            print(f"It doesn't start with {computer[-1]}! Try again!") 
        else:
            check_result = check_def(player)
            if check_result:
                

                computer = requests.get(
                    f"https://random-word-api.vercel.app/api?letter={player[-1]}").json()[0]

                print(
                    f"Computer: {computer}, now type a word beginning with {computer[-1]}, or type 'checkdef' for the definition of the word")



